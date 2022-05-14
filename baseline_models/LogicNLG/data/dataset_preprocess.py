# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:42:21 2020

@author: shank
"""

import numpy as np
from os.path import isfile, join
import re
import pandas as pd
import json


file_no=0
ref_no=file_no
#train_data_load
mypath=".\C2T_data"
summary = np.loadtxt(join(mypath,"train\\trainOriginalSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
templ_summary = np.loadtxt(join(mypath,"train\\trainSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
title = np.loadtxt(join(mypath,"train\\trainTitle.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data = np.loadtxt(join(mypath,"train\\trainData.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)


#convert each line in data to a table and store as csv file in  data/all_csv.



def convert_list_to_dict(axis_value_list):
    table_dict={}
    for item in axis_value_list:
        colname = re.findall(r'.*?\|',item)[0][:-1]
        colval = re.findall(r'.*?\|',item)[1][:-1]
        if colname not in table_dict:
            table_dict[colname]=[colname];table_dict[colname].append(colval)
        else:
            table_dict[colname].append(colval)
    return  table_dict

def get_col_list(templ_string):
    lst = templ_string.split()
    col_list = []
    for tok in lst:
            if 'templateValue' in tok:
                start = tok.find('[')
                end = tok.find(']')
                col_list.append(int(tok[start+1:end]))
            if 'templateYValue' in tok:
                col_list.append(1)
            if 'templateXValue' in tok:
                col_list.append(0)
            if 'templateLabel' in tok:
                start = tok.find('[')
                end = tok.find(']')
                col_list.append(int(tok[start+1:end]))
            if 'templateYLabel' in tok:
                col_list.append(1)
            if 'templateXLabel' in tok:
                col_list.append(0)
    
    if col_list == []:
        col_list.append(0)
    
    
    return list(set(col_list))
    
def convert_to_generic_templates(templ_string):
    lst = templ_string.split()
    for tok in lst:
        if 'template' in tok:
            lst[lst.index(tok)] = "[ENT]"
    return " ".join(lst)

for tableIndex in range(len(data)):
    axis_value_list=[re.findall(r".*?\|.*?[\|]",item)[0] for item in  data[tableIndex].split()]
    table_dict = convert_list_to_dict(axis_value_list)
    table_frame = pd.DataFrame(table_dict)
    table_frame.to_csv(join("all_csv",str(file_no)+".csv"),encoding='utf8',header=None,index=False)
    #np.savetxt(join("all_csv",str(file_no)+".csv"), table_frame, delimiter='#', fmt='%s',encoding='utf8')
    file_no+=1


gold_dict={}


for item in zip(summary,title,templ_summary):
    col_list = get_col_list(item[2])
    templ_string = convert_to_generic_templates(item[2])
    gold_dict[str(ref_no) + ".csv"] = []
    gold_dict[str(ref_no) + ".csv"].append([str(item[0]),col_list,str(item[1]),templ_string])
    ref_no+=1
    
with open('./input_tokenization/train_lm.json', 'w') as json_file:
        json.dump(gold_dict, json_file)    
 
    
 
    
 


#--------------------------------test data/summary/title load -----------------------



ref_no=file_no

#test_data_load
mypath=".\C2T_data"
summary = np.loadtxt(join(mypath,"test\\testOriginalSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
templ_summary = np.loadtxt(join(mypath,"test\\testSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
title = np.loadtxt(join(mypath,"test\\testTitle.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data = np.loadtxt(join(mypath,"test\\testData.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)


#convert each line in data to a table and store as csv file in  data/all_csv.
# file no. will be continuation of train data since for logicnlg all data csv files should be in one folder


def convert_list_to_dict(axis_value_list):
    table_dict={}
    for item in axis_value_list:
        colname = re.findall(r'.*?\|',item)[0][:-1]
        colval = re.findall(r'.*?\|',item)[1][:-1]
        if colname not in table_dict:
            table_dict[colname]=[colname];table_dict[colname].append(colval)
        else:
            table_dict[colname].append(colval)
    return  table_dict




for tableIndex in range(len(data)):
    axis_value_list=[re.findall(r".*?\|.*?[\|]",item)[0] for item in  data[tableIndex].split()]
    table_dict = convert_list_to_dict(axis_value_list)
    table_frame = pd.DataFrame(table_dict)
    table_frame.to_csv(join("all_csv",str(file_no)+".csv"),encoding='utf8',header=None,index=False)
    #np.savetxt(join("all_csv",str(file_no)+".csv"), table_frame, delimiter='#', fmt='%s',encoding='utf8')
    file_no+=1


gold_dict={}


for item in zip(summary,title,templ_summary):
    col_list = get_col_list(item[2])
    templ_string = convert_to_generic_templates(item[2])
    gold_dict[str(ref_no) + ".csv"] = []
    gold_dict[str(ref_no) + ".csv"].append([str(item[0]),col_list,str(item[1]),templ_string])
    ref_no+=1
    
with open('./input_tokenization/test_lm.json', 'w') as json_file:
        json.dump(gold_dict, json_file)    








#--------------------------------validation data/summary/title load -----------------------



ref_no=file_no

#validation_data_load
mypath=".\C2T_data"
summary = np.loadtxt(join(mypath,"valid\\validOriginalSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
templ_summary = np.loadtxt(join(mypath,"valid\\validSummary.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
title = np.loadtxt(join(mypath,"valid\\validTitle.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)
data = np.loadtxt(join(mypath,"valid\\validData.txt"), comments=None, delimiter="\n",dtype=str,encoding='utf8', unpack=False)


#convert each line in data to a table and store as csv file in  data/all_csv.
# file no. will be continuation of train data since for logicnlg all data csv files should be in one folder


def convert_list_to_dict(axis_value_list):
    table_dict={}
    for item in axis_value_list:
        colname = re.findall(r'.*?\|',item)[0][:-1]
        colval = re.findall(r'.*?\|',item)[1][:-1]
        if colname not in table_dict:
            table_dict[colname]=[colname];table_dict[colname].append(colval)
        else:
            table_dict[colname].append(colval)
    return  table_dict




for tableIndex in range(len(data)):
    axis_value_list=[re.findall(r".*?\|.*?[\|]",item)[0] for item in  data[tableIndex].split()]
    table_dict = convert_list_to_dict(axis_value_list)
    table_frame = pd.DataFrame(table_dict)
    table_frame.to_csv(join("all_csv",str(file_no)+".csv"),encoding='utf8',header=None,index=False)
    #np.savetxt(join("all_csv",str(file_no)+".csv"), table_frame, delimiter='#', fmt='%s',encoding='utf8')
    file_no+=1


gold_dict={}


for item in zip(summary,title,templ_summary):
    col_list = get_col_list(item[2])
    templ_string = convert_to_generic_templates(item[2])
    gold_dict[str(ref_no) + ".csv"] = []
    gold_dict[str(ref_no) + ".csv"].append([str(item[0]),col_list,str(item[1]),templ_string])
    ref_no+=1
    
with open('./input_tokenization/val_lm.json', 'w') as json_file:
        json.dump(gold_dict, json_file)    

 
    