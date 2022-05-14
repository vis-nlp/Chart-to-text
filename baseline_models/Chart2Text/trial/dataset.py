import os
import numpy as np
import torch.nn as nn
import torch
import pandas as pd
from PIL import Image

class VisionTapasDataset(torch.utils.data.Dataset):
    def __init__(self, instances, tables, images_folder, tokenizer, feature_extractor):
        # Qa pairs.
        self.instances = instances
        self.tables = tables
        self.images_folder = images_folder
        self.tokenizer = tokenizer
        self.feature_extractor = feature_extractor

    def __getitem__(self, idx):
        instance = self.instances[idx]
        image_index = instance["image_index"]
        question = instance["question"]
        answer = instance["answer"]

        # Process table
        df = self.tables[str(image_index)]
        new_df = df.copy()#.iloc[:, 1:].copy()
        new_df = new_df.astype(str)
        encoding = self.tokenizer(table=new_df, queries=[question], padding="max_length", truncation=True, return_tensors="pt")

        image = Image.open(self.images_folder + str(image_index) + ".png").convert("RGB")
        vis_inputs = self.feature_extractor(images=image, return_tensors="pt")

        item = {key: val.squeeze(0) for key, val in encoding.items()}
        for key, val in vis_inputs.items():
            item[key] = val.squeeze(0)
        item['labels'] = torch.tensor(answer)
        return item

    def __len__(self):
        return len(self.instances)

class T5Dataset(torch.utils.data.Dataset):
    def __init__(self, instances, tokenizer):
        # Qa pairs.
        self.instances = instances
        self.inputs = instances["Input"].values
        self.outputs = instances["Output"].values
        self.tokenizer = tokenizer

    def __getitem__(self, idx):
        input = self.inputs[idx]
        output = self.outputs[idx]
        inputs = self.tokenizer(str(input), padding="max_length", truncation=True, return_tensors='pt')
        labels = self.tokenizer(str(output), padding="max_length", truncation=True, return_tensors='pt').input_ids

        inputs['labels'] = labels
        for k, v in inputs.items():
            inputs[k] = v.squeeze(0)

        return inputs

    def __len__(self):
        return len(self.inputs)

class T5BboxesDataset(torch.utils.data.Dataset):
    def __init__(self, instances, tokenizer):
        # Qa pairs.
        self.instances = instances
        self.inputs = instances["Input"].values
        self.outputs = instances["Output"].values
        self.bboxes = instances['bboxes_text'].values
        #print(self.bboxes[0])
        self.tokenizer = tokenizer

    def __getitem__(self, idx):
        input = self.inputs[idx]
        output = self.outputs[idx]
        bboxes_text = self.bboxes[idx]
        bboxes_pre = str(bboxes_text).split("</s>")
        bboxes = []
        for bbox_pre in bboxes_pre:
            if bbox_pre == '':
                continue
            bbox = [float(x) for x in bbox_pre.split(",")]
            if len(bbox) != 4:
                continue
            bboxes.append(bbox)
        bboxes = np.array(bboxes)

        inputs = self.tokenizer(str(input), padding="max_length", truncation=True, return_tensors='pt')
        input_ids = inputs.input_ids
        # Prepare the bounding boxes tensor.
        seq_length = 512
        sep_indices = [-1] + (input_ids[0] == 1).nonzero(as_tuple=True)[0].tolist()
        padd_bbox = np.array([0, 0, 0, 0])
        bboxes_input_array = []
        for i in range(0, len(sep_indices) - 1):
            st_idx = sep_indices[i]
            end_idx = sep_indices[i + 1]
            bboxes_input_array.append(np.repeat(bboxes[i][np.newaxis, :], end_idx - st_idx, axis=0))
        #bboxes_input_array.append(np.repeat(padd_bbox[np.newaxis, :], seq_length - sep_indices[-1] - 1, axis=0))
        bboxes_num = sum([len(x) for x in bboxes_input_array])
        while bboxes_num < seq_length:
            bboxes_input_array.append(padd_bbox[np.newaxis, :])
            bboxes_num = sum([len(x) for x in bboxes_input_array])
        bboxes_input_tensor = torch.FloatTensor(np.concatenate(bboxes_input_array, axis=0)).unsqueeze(0)
        inputs['bboxes'] = bboxes_input_tensor
        ###

        labels = self.tokenizer(str(output), padding="max_length", truncation=True, return_tensors='pt').input_ids
        inputs['labels'] = labels
        for k, v in inputs.items():
            inputs[k] = v.squeeze(0)

        return inputs

    def __len__(self):
        return len(self.inputs)
class VisionT5Dataset(torch.utils.data.Dataset):
    def __init__(self, instances, tokenizer, feature_extractor, images_folder):
        # Qa pairs.
        self.instances = instances
        self.inputs = instances["Input"].values
        self.outputs = instances["Output"].values
        self.images_indices = instances["Image Index"].values
        self.tokenizer = tokenizer

        self.images_folder = images_folder
        self.feature_extractor = feature_extractor


    def __getitem__(self, idx):
        input = self.inputs[idx]
        output = self.outputs[idx]
        image_index = self.images_indices[idx]

        # Image
        image = Image.open(self.images_folder + str(image_index) + ".png").convert("RGB")
        pixel_values = self.feature_extractor(images=image, return_tensors="pt")['pixel_values']

        # T5 Input
        inputs = self.tokenizer(input, max_length=391, padding="max_length", truncation=True, return_tensors='pt')
        batch_size, sq_length = inputs['attention_mask'].size()
        inputs['attention_mask'] = torch.cat((torch.ones((batch_size, 121)), inputs['attention_mask']), dim=1)
        inputs['pixel_values'] = pixel_values

        # T5 outputs
        outputs = self.tokenizer(str(output), padding="max_length", return_tensors='pt')
        inputs['labels'] = outputs.input_ids
        #inputs['decoder_attention_mask'] = outputs['attention_mask']
        #inputs['decoder_inputs_embeds '] = self.t5_embeddings(outputs['input_ids'].to('cuda')).to('cpu')

        for k, v in inputs.items():
            inputs[k] = v.squeeze(0)

        return inputs

    def __len__(self):
        return len(self.inputs)
