# -*- coding: utf-8 -*-


with open("statista/c2t_data/scores", 'r', encoding='utf-8') as actualfile:
            scores = actualfile.readlines()


print(sum([float(i[:-1]) for i in scores])/len(scores))