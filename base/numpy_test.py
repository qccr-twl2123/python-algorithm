#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  numpy as np

dataset  = [[1,0,1,0],[1,0,1,1],[1,1,1,0]]
print dataset
dataset = np.array(dataset)
print dataset

# sum axis=none 全部相加 0 按列相加 1 按行相加
a = np.sum(dataset,0)+1
print a
# 定时
sub_dataset =[[1,0,1,0],[1,0,1,1]]
sub_dataset = np.array(sub_dataset)
b = np.sum(sub_dataset) +2

print b

cond_prob_vect = np.log((np.sum(sub_dataset,0)+1) / np.sum(dataset)+2)


print  cond_prob_vect