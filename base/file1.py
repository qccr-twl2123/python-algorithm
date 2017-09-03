#!/usr/bin/python

import re
import collections
import numpy as np

def get_doc_vector(words,vocabulary):
    doc_vect = [0]*len(vocabulary)
    for word in words:
        if word in vocabulary:
            idx = vocabulary.index(word)
            doc_vect[idx] = 1
    return doc_vect

def parse_line(line):
    cls = line.split(",")[-1].strip()
    content = ",".join(line.split(","))[:-1]
    word_vect = [word.lower() for word in re.split(r"\W+",content) if word]
    return word_vect,cls

def parse_file(filename):
    vocabulary,word_vects,classes=[],[],[]
    with open(filename,"r") as f:
        for line in f:
            if line:
                word_vect,cls = parse_line(line)
                vocabulary.extend(word_vect)
                word_vects.append(word_vect)
                classes.append(cls)
                vocabulary = list(set(vocabulary))
    return vocabulary, word_vects,classes

def train(self,dataset,classes):
    sub_dataset = collections.defaultdict(lambda :[])
    cls_cnt = collections.defaultdict(lambda :0)
    for doc_vect,cls in zip(dataset,classes):
        sub_dataset.append(doc_vect)
        cls_cnt[cls] +=1

    #计算类型概率
    cls_probs = {k:v/len(classes) for k,v in cls_cnt.items()}

    #计算不同类型条件概率
    cond_probs ={}
    dataset = np.array(dataset)

    for cls, sub_dataset in sub_dataset.items():
        sub_dataset = np.array(sub_dataset)
        cond_prob_vect = np.log((np.sum(sub_dataset,0)+1) / np.sum(dataset)+2)
        cond_probs[cls] = cond_prob_vect

    return cond_probs,cls_probs

def classify(self,doc_vect,cond_probs,cls_probs):
    pred_probs = {}
    for cls,cls_prob in cls_probs.items():
        cond_prob_vect = cond_probs[cls]
        pred_probs[cls] = np.sum(cond_prob_vect * doc_vect) + np.log(cls_prob)
    return max(pred_probs,pred_probs.get())


if __name__=="__main__":
    vocabulary,word_vects,classes = parse_file("demo.text")
    print vocabulary,word_vects,classes
    doc_vect = get_doc_vector(word_vects[1],vocabulary)
    print doc_vect