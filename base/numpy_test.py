#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  numpy as np

dataset  = [[1,0,1,0],[1,0,1,1],[1,1,1,0]]
print dataset
#将列表转换成多维数组
dataset = np.array(dataset)
print dataset

#numpy.sum 数组加法
# sum axis=none 全部相加 0 按列相加 1 按行相加
a = np.sum(dataset,0)+1
print a

sub_dataset =[[1,0,1,0],[1,0,1,1]]
sub_dataset = np.array(sub_dataset)
b = np.sum(sub_dataset) +2
print b

cond_prob_vect = np.log((np.sum(sub_dataset,0)+1.0) / np.sum(dataset)+2)

# print (np.sum(sub_dataset,0)+1.0) / (np.sum(dataset)+2);
# print (np.sum(sub_dataset,0)+1.0),(np.sum(dataset)+2)
# print np.log([7,7])

print  cond_prob_vect