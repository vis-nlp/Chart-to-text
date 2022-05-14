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




with open(train_file) as f:
  train = json.load(f)


with open(val_file) as f:
  val = json.load(f)


with open(test_file) as f:
  test = json.load(f)




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





