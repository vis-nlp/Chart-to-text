# -*- coding: utf-8 -*-

import json

with open("statista/c2t_data/testOriginalSummary.txt", 'r',encoding='utf8') as actualfile:
            actual = actualfile.readlines()
            

with open("statista/c2t_data/generated-p80.txt", 'r',encoding='utf8') as generatedfile:
            generated = generatedfile.readlines()
    
output_list_actual = []
output_list_generated = []
count = 0;
for i,j in zip(actual,generated):
    data_actual = { "image_id":count, "caption":i }; 
    data_generated = { "image_id":count, "caption":j };
    count+=1;
    output_list_actual.append(data_actual)
    output_list_generated.append(data_generated)
    #json_data = json.dumps(data)
    # output_dict['id'] = count; count+=1;
    # output_dict['text'] = i;
    # output_dict['claim'] = j;


      
with open('statista/c2t_data/testOriginalSummary.json','w') as f:
    json.dump(output_list_actual,f)


with open('statista/c2t_data/generated-p80.json','w') as f:
    json.dump(output_list_generated,f)




# with open(input_file, "r", encoding="utf-8") as f:
#            a = json.load(f)