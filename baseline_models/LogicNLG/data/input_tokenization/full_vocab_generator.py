
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:44:05 2020

@author: shank
"""

import pandas as pd
# from collections import Counter
from os import listdir
from os.path import isfile, join
# import copy
import json



max_len=0
all_list=[]

#train_data_load
vocab_file="../vocab_tokenization/bpe_tokenizer-vocab.json"
datapath="../all_csv/"

with open(vocab_file, encoding="utf8") as f:
            vocab = json.load(f)


datafiles = [f for f in listdir(datapath) if isfile(join(datapath, f))]

for table in datafiles:
    d = pd.read_csv(datapath + table,encoding='utf8')
    if len(d) > max_len: max_len = len(d)
    # all_list = all_list + [str(cell) for row in d.values.tolist() for  cell in row]


# with open('train_lm.json',encoding="utf8") as f:
#             gold_train = json.load(f)
# all_list = all_list + [str(token) for row in gold_train.values() for  ref in row[0] if type(ref)==str for token in ref.split()]



# with open('test_lm.json',encoding="utf8") as f:
#             gold_test = json.load(f)
# all_list = all_list + [str(token) for row in gold_test.values() for  ref in row[0] if type(ref)==str for token in ref.split()]


# with open('val_lm.json',encoding="utf8") as f:
#             gold_val = json.load(f)
# all_list = all_list + [str(token) for row in gold_val.values() for  ref in row[0] if type(ref)==str for token in ref.split()]






# cnt = Counter()
# for word in all_list:
#     cnt[word] += 1



# full_vocab_list = [ent[0] for ent in cnt.most_common()]

vocab["<PAD>"] = len(vocab);
vocab["<SEP>"] = len(vocab);
vocab["<SOS>"] = len(vocab);
vocab["<EOS>"] = len(vocab);
vocab["<UNK>"] = len(vocab);
vocab["<UNK>"] = len(vocab);
vocab["#0"] = len(vocab);







for i in range(max_len):
    vocab["#"+str(i+1)] = len(vocab);

# vocab_dict=copy.deepcopy(full_vocab_dict)


# for key in full_vocab_list:
#     full_vocab_dict[key]=k
#     if k < len(full_vocab_list)*.3:
#         vocab_dict[key]=k
#     k+=1;

with open('vocab.json', 'w',encoding='utf8') as json_file:
        json.dump(vocab, json_file)    

vocab["#"+str(i+2)] = len(vocab);

with open('full_vocab.json', 'w',encoding='utf8') as json_file:
        json.dump(vocab, json_file)    

