# -*- coding: utf-8 -*-


import json



from tokenizers import CharBPETokenizer

# Initialize a tokenizer
vocab = "../vocab_tokenization/bpe_tokenizer-vocab.json"
merges = "../vocab_tokenization/bpe_tokenizer-merges.txt"
tokenizer = CharBPETokenizer(vocab,merges)

# And then encode:
# encoded = tokenizer.encode("I can feel the magic, can you?")
# print(encoded.ids)
# print(encoded.tokens)


train_file = "train_lm.json"
val_file = "val_lm.json"
test_file = "test_lm.json"


train_bbox_dir = "../C2T_data/train/trainBbox.txt"
val_bbox_dir = "../C2T_data/valid/validBbox.txt"
test_bbox_dir = "../C2T_data/test/testBbox.txt"


with open(train_file) as f:
  train = json.load(f)


with open(val_file) as f:
  val = json.load(f)


with open(test_file) as f:
  test = json.load(f)




with open(train_bbox_dir, 'r', encoding='utf-8') as file:
            train_bbox = file.readlines()

with open(val_bbox_dir, 'r', encoding='utf-8') as file:
            val_bbox = file.readlines()

with open(test_bbox_dir, 'r', encoding='utf-8') as file:
            test_bbox = file.readlines()






for entry in train:
    actual_summary = train[entry][0][0]
    train[entry][0][0] = " ".join(tokenizer.encode(actual_summary).tokens)
    title = train[entry][0][2]
    train[entry][0][2] = " ".join(tokenizer.encode(title).tokens)


with open('train_lm_encoded.json', 'w',encoding='utf8') as json_file:
        json.dump(train, json_file)    


for entry in val:
    actual_summary = val[entry][0][0]
    val[entry][0][0] = " ".join(tokenizer.encode(actual_summary).tokens)
    title = val[entry][0][2]
    val[entry][0][2] = " ".join(tokenizer.encode(title).tokens)


with open('val_lm_encoded.json', 'w',encoding='utf8') as json_file:
        json.dump(val, json_file)    



for entry in test:
    actual_summary = test[entry][0][0]
    test[entry][0][0] = " ".join(tokenizer.encode(actual_summary).tokens)
    title = test[entry][0][2]
    test[entry][0][2] = " ".join(tokenizer.encode(title).tokens)


with open('test_lm_encoded.json', 'w',encoding='utf8') as json_file:
        json.dump(test, json_file)    




for i in range(len(train_bbox)):
    train_bbox[i]=" ".join(tokenizer.encode(train_bbox[i]).tokens)


for i in range(len(val_bbox)):
    val_bbox[i]=" ".join(tokenizer.encode(val_bbox[i]).tokens)


for i in range(len(test_bbox)):
    test_bbox[i]=" ".join(tokenizer.encode(test_bbox[i]).tokens)




with open('test_bbox_encoded.txt', 'w', encoding='utf-8') as file:
            for item in test_bbox:
                file.write("%s\n" % item)

with open('train_bbox_encoded.txt', 'w', encoding='utf-8') as file:
            for item in train_bbox:
                file.write("%s\n" % item)

with open('valid_bbox_encoded.txt', 'w', encoding='utf-8') as file:
            for item in val_bbox:
                file.write("%s\n" % item)






