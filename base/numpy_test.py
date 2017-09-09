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


print "-----------^^^^^^^^-----------"
x = np.arange(72).reshape((24,3)) # 创建一个24行3列的新数组
train_set1, test_sets1, val_sets1 = np.split(x, 3) # 将数组平均分为3份

print train_set1
train_set2, test_sets2, val_sets2 = np.split(x, [int(0.6*x.shape[0]), int(0.9*x.shape[0])]) # 60%训练集,30%测试集,10%验证集
print ('record of each set - equal arrays: ')
print ('train_set1: %d, test_sets1: %d, val_sets1: %d'%(train_set1.shape[0], test_sets1.shape[0], val_sets1.shape[0]))
print (40*'-')
print ('record of each set - % arrays: ')
print ('train_set2: %d, test_sets2: %d, val_sets2: %d'%(train_set2.shape[0], test_sets2.shape[0], val_sets2.shape[0]))