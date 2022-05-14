# -*- coding: utf-8 -*-

import pandas as pd
import os

# datadir="../data/valid/validData.txt"
output_datadir="../data/test/testDataOCR.txt"
output_captiondir="../data/test/testOriginalSummary.txt"
output_titledir="../data/test/testTitle.txt"
output_datalabeldir="../data/test/testDataLabel.txt"
output_captionlabeldir="../data/test/testSummaryLabel.txt"
mappingdir="../../../../c2t_dataset_pew/test_index_mapping.csv"

ocrdata_twocol_dir= "../../../../c2t_dataset_pew/dataset/data/" 
ocrdata_multicol_dir= "../../../../c2t_dataset_pew/dataset/multiColumn/data/" 
# data_twocol_dir= "../../../../c2t_dataset_pew/dataset/data/" 
# data_multicol_dir= "../../../../c2t_dataset_pew/dataset/multiColumn/data/" 


captions_twocol_dir= "../../../../c2t_dataset_pew/dataset/captions/" 
captions_multicol_dir= "../../../../c2t_dataset_pew/dataset/multiColumn/captions/" 

titles_twocol_dir= "../../../../c2t_dataset_pew/dataset/titles/" 
titles_multicol_dir= "../../../../c2t_dataset_pew/dataset/multiColumn/titles/" 




# with open(datadir, 'r', encoding='utf-8') as datafile:
#         data = datafile.readlines()

data=[]
captions=[]
titles=[]
data_labels=[]
caption_labels=[]


mapping = pd.read_csv(mappingdir,encoding='utf8')







ocrdata_twocol=os.listdir(ocrdata_twocol_dir)
ocrdata_multicol=os.listdir(ocrdata_multicol_dir)
# data_twocol=os.listdir(data_twocol_dir)
# data_multicol=os.listdir(data_multicol_dir)



# counter = 0

def extract_ocrdata(data_text,caption_text):
    tokens=["_".join(i.strip().split(" ")) for i in data_text.split(" | ")]
    multiword_tokens=[i.strip() for i in data_text.split(" | ")]
    
    data_list=[]
    
    for token in tokens:
        data_list.append("entity|"+token.replace("|","/")+"|feat|chart")
    
    
    data_string = " ".join(data_list)
    
    data_label_list = [0]*len(data_list)
    caption_list = caption_text.split(" ")
    caption_label_list = [0]*len(caption_list)
    
    for token in caption_list:
        if token in multiword_tokens:
            # print(token)
            caption_label_list[caption_list.index(token)]=1
            data_label_list[multiword_tokens.index(token)]=1
    
    caption_label_string = " ".join(str(v) for v in caption_label_list)
    data_label_string = " ".join(str(v) for v in data_label_list)
    
    return data_string,data_label_string,caption_label_string


# def extract_data(table,caption_text):
    
#     data_list=[]
#     multiword_tokens=[]
#     for index,row in table.iterrows():
#         for col_no in range(len(row)):
#             if col_no==0:
#                 data_list.append(table.columns[col_no].replace(" ","_").replace("\n","_")+"|"+str(row[col_no]).replace(" ","_").replace("\n","_")+"|x|chart")
#             else:
#                 data_list.append(table.columns[col_no].replace(" ","_").replace("\n","_")+"|"+str(row[col_no]).replace(" ","_").replace("\n","_")+"|y|chart")
            
#             multiword_tokens.append(row[col_no])
            
#     data_string = " ".join(data_list).replace("\n"," ").replace("\xa0","_")
    
    
    
    
    
    
    data_label_list = [0]*len(data_list)
    caption_list = caption_text.split(" ")
    caption_label_list = [0]*len(caption_list)
    
    for token in caption_list:
        if token in multiword_tokens:
            # print(token)
            caption_label_list[caption_list.index(token)]=1
            data_label_list[multiword_tokens.index(token)]=1
    
    caption_label_string = " ".join(str(v) for v in caption_label_list)
    data_label_string = " ".join(str(v) for v in data_label_list)
    
    
    
    
    return data_string,data_label_string,caption_label_string





for index,row in mapping.iterrows():
    if 'two_col' in row[0]:
        if row[0][8:] in ocrdata_twocol:
            with open(ocrdata_twocol_dir+row[0][8:], 'r', encoding='utf-8') as datafile:
                data_string = datafile.read()
            with open(captions_twocol_dir+row[0][8:], 'r', encoding='utf-8') as captionfile:
                caption_string = captionfile.read()
            with open(titles_twocol_dir+row[0][8:], 'r', encoding='utf-8') as titlefile:
                title_string = titlefile.read()
            
            processed_data,data_label,caption_label = extract_ocrdata(data_string,caption_string)
            data.append(processed_data)
            data_labels.append(data_label)
            caption_labels.append(caption_label)
            captions.append(caption_string)
            titles.append(title_string)
                
        # elif row[0][8:].replace(".txt",".csv") in data_twocol:
        #     with open(captions_twocol_dir+row[0][8:], 'r', encoding='utf-8') as captionfile:
        #         caption_string = captionfile.read()
        #     with open(titles_twocol_dir+row[0][8:], 'r', encoding='utf-8') as titlefile:
        #         title_string = titlefile.read()
                
        #     table = pd.read_csv(data_twocol_dir+row[0][8:].replace(".txt",".csv"),encoding='utf-8')
        #     processed_data,data_label,caption_label = extract_data(table,caption_string)
                 
        #     data.append(processed_data)
        #     data_labels.append(data_label)
        #     caption_labels.append(caption_label)
        #     captions.append(caption_string)
        #     titles.append(title_string)
            
        else:
            raise Exception("could not find file,",row[0])
                
            
    elif 'multi_col' in row[0]:
        if row[0][10:] in ocrdata_multicol:
            with open(ocrdata_multicol_dir+row[0][10:], 'r', encoding='utf-8') as datafile:
               data_string = datafile.read()
            with open(captions_multicol_dir+row[0][10:], 'r', encoding='utf-8') as captionfile:
                caption_string = captionfile.read()
            with open(titles_multicol_dir+row[0][10:], 'r', encoding='utf-8') as titlefile:
                title_string = titlefile.read()
            
            processed_data,data_label,caption_label = extract_ocrdata(data_string,caption_string)
            data.append(processed_data)
            data_labels.append(data_label)
            caption_labels.append(caption_label)
            captions.append(caption_string)
            titles.append(title_string)
                
        # elif row[0][10:].replace(".txt",".csv") in data_multicol:
        #     with open(captions_multicol_dir+row[0][10:], 'r', encoding='utf-8') as captionfile:
        #         caption_string = captionfile.read()
        #     with open(titles_multicol_dir+row[0][10:], 'r', encoding='utf-8') as titlefile:
        #         title_string = titlefile.read()
                
        #     table = pd.read_csv(data_multicol_dir+row[0][10:].replace(".txt",".csv"),encoding='utf-8')
        #     processed_data,data_label,caption_label = extract_data(table,caption_string)
                 
        #     data.append(processed_data)
        #     data_labels.append(data_label)
        #     caption_labels.append(caption_label)
        #     captions.append(caption_string)
        #     titles.append(title_string)
                
        else:
            raise Exception("could not find file,",row[0])


with open(output_datadir, mode='wt', encoding='utf8') as file:
        file.writelines("%s\n" % line for line in data)

'''
with open(output_captiondir, mode='wt', encoding='utf8') as file:
        file.writelines("%s" % line for line in captions)

with open(output_titledir, mode='wt', encoding='utf8') as file:
        file.writelines("%s" % line for line in titles)


with open(output_datalabeldir, mode='wt', encoding='utf8') as file:
        file.writelines("%s\n" % line for line in data_labels)


with open(output_captionlabeldir, mode='wt', encoding='utf8') as file:
        file.writelines("%s\n" % line for line in caption_labels)

'''

