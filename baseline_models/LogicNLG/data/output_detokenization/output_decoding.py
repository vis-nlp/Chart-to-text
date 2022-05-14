# -*- coding: utf-8 -*-




import json
import pandas as pd
# from collections import Counter
from os import listdir
from os.path import isfile, join
# import copy
import json


from tokenizers import CharBPETokenizer

# Initialize a tokenizer
vocab = "../vocab_tokenization/bpe_tokenizer-vocab.json"
merges = "../vocab_tokenization/bpe_tokenizer-merges.txt"
tokenizer = CharBPETokenizer(vocab, merges)

# And then encode:
# encoded = tokenizer.encode("I can feel the magic, can you?")
# print(encoded.ids)
# print(encoded.tokens)


results_file = "statista/field_infusing.json"
# val_file = "../val_lm.json"
# test_file = "../test_lm.json"


with open(results_file) as f:
  results = json.load(f)


# with open(val_file) as f:
#   val = json.load(f)


# with open(test_file) as f:
#   test = json.load(f)




# for entry in train:
#     actual_summary = train[entry][0][0]
#     train[entry][0][0] = " ".join(tokenizer.encode(actual_summary).tokens)
#     title = train[entry][0][2]
#     train[entry][0][2] = " ".join(tokenizer.encode(title).tokens)


# with open('train_lm_encoded.json', 'w') as json_file:
#         json.dump(train, json_file)    


# for entry in val:
#     actual_summary = val[entry][0][0]
#     val[entry][0][0] = " ".join(tokenizer.encode(actual_summary).tokens)
#     title = val[entry][0][2]
#     val[entry][0][2] = " ".join(tokenizer.encode(title).tokens)


# with open('val_lm_encoded.json', 'w') as json_file:
#         json.dump(val, json_file)    



# for entry in test:
#     actual_summary = test[entry][0][0]
#     test[entry][0][0] = " ".join(tokenizer.encode(actual_summary).tokens)
#     title = test[entry][0][2]
#     test[entry][0][2] = " ".join(tokenizer.encode(title).tokens)


# with open('test_lm_encoded.json', 'w') as json_file:
#         json.dump(test, json_file)    

datapath="../all_csv/"

datafiles = [f for f in listdir(datapath) if isfile(join(datapath, f))]


max_len=0

for table in datafiles:
    d = pd.read_csv(datapath + table,encoding='utf8')
    if len(d) > max_len: max_len = len(d)


extra_tokens=[]


extra_tokens.append("<PAD>")
extra_tokens.append("<SEP>")
extra_tokens.append("<SOS>")
extra_tokens.append("<EOS>")
extra_tokens.append("<UNK>")
extra_tokens.append("<UNK>")
extra_tokens.append("#0")







for i in range(max_len):
    extra_tokens.append("#"+str(i+1))

extra_tokens.append("#"+str(max_len+1))
tokenizer.add_tokens(extra_tokens)


for entry in results:
    text = results[entry][0]
    lst = []
    for token in text.split():
        lst.append(tokenizer.token_to_id(token))
    results[entry][0] = tokenizer.decode(lst)
    




with open("statista/field_infusing_decoded.json", 'w') as f:
    json.dump(results, f)








