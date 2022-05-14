# -*- coding: utf-8 -*-

import pandas as pd
import os
import re
import json

output_bboxdir="../data/valid/validBbox.txt"
mappingdir="../../../../c2t_dataset_pew/val_index_mapping.csv"
twocol_bbox_dir="../../../../c2t_dataset_pew/dataset/bboxes/"
multicol_bbox_dir="../../../../c2t_dataset_pew/dataset/multiColumn/bboxes/"
ocr_datadir="../data/valid/validDataOCR.txt"




bboxes=[]

mapping = pd.read_csv(mappingdir,encoding='utf8')
# bboxes = pd.read_csv(bbox_dir,encoding='utf8')



with open(ocr_datadir, 'r', encoding='utf-8') as file:
                ocrdata_list= file.readlines()






def extract_bboxes(bbox_list,ocrdata_list_text):
    
    processed_bboxes=[]
    # bbox_list = bbox_text.split("</s>")
    # bbox_list = list(filter(None, bbox_list))
    if len(bbox_list) == len(ocrdata_list_text.split(" ")): 
        for row in bbox_list:
            items = [str(round(float(i))) for i in row['bounding_box']]
            processed_bboxes.append("|".join(items))
    else:                                                       #condition triggers when taking bbox data is unavailable/incomplete
            processed_bboxes= " ".join(['0|0|0|0']*len(ocrdata_list_text.split(" ")))
            return processed_bboxes
    
    
    return " ".join(processed_bboxes)
    
    





for index,row in mapping.iterrows():
    # if 'two_col' in row[0]:
        file_no = int(re.findall(r'\d+', row[0])[0])
        #if file_no in bbox_mapping['Image Index'].tolist():
            #assert file_no == bbox_mapping.iloc[index]['Image Index']
        if 'two_col' in row[0]:
            with open(twocol_bbox_dir+str(file_no)+'.json',encoding='utf8') as f:
                bbox_list = json.load(f)
        elif 'multi_col' in row[0]:
            with open(multicol_bbox_dir+str(file_no)+'.json',encoding='utf8') as f:
                bbox_list = json.load(f)
        #bbox_text = bbox_mapping.iloc[index]['bboxes_text']
        processed_bboxes = extract_bboxes(bbox_list,ocrdata_list[index])
            
            
        # else:
        #     print(file_no)
            
            
            # processed_bboxes= " ".join(['0|0|0|0']*len(bboxes_list[index].split(" ")))
        
        bboxes.append(processed_bboxes)
            
            
            
            
            

            
            


with open(output_bboxdir, mode='wt', encoding='utf8') as file:
        file.writelines("%s\n" % line for line in bboxes)



