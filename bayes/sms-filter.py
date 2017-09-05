#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import collections
import numpy as np
import matplotlib.pyplot as plt

def get_doc_vector(words,vocabulary):
    doc_vect = [0]*len(vocabulary)
    for word in words:
        if word in vocabulary:
            idx = vocabulary.index(word)
            doc_vect[idx] = 1
    return doc_vect

def parse_line(line):
    cls = line.split(",")[0].strip()
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

def train(dataset,classes):
    sub_dataset = collections.defaultdict(lambda :[])
    cls_cnt = collections.defaultdict(lambda :0)
    print zip(dataset,classes)
    for doc_vect,cls in zip(dataset,classes):
        sub_dataset[cls].append(doc_vect)
        cls_cnt[cls] += 1

    cls_probs = {k: float(v)/len(classes) for k, v in cls_cnt.items()}

    cond_probs ={}
    dataset = np.array(dataset)
    for cls, sub_dataset in sub_dataset.items():
        sub_dataset = np.array(sub_dataset)
        cond_prob_vect = np.log((np.sum(sub_dataset,0)+1.0) / np.sum(dataset)+2)
        cond_probs[cls] = cond_prob_vect

    return cond_probs,cls_probs

def classify(doc_vect,cond_probs,cls_probs):
    pred_probs = {}
    for cls,cls_prob in cls_probs.items():
        cond_prob_vect = cond_probs[cls]
        pred_probs[cls] = np.sum(cond_prob_vect * doc_vect) + np.log(cls_prob)
    return max(pred_probs,key=pred_probs.get)

def chart_show(cond_probs, cls_probs):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for cls, probs in cond_probs.items():
        ax.scatter(np.arange(0,len(probs)),
               probs*cls_probs[cls],
               label=cls,
               alpha=0.3)
        ax.legend()
    plt.show()


if __name__=="__main__":
    vocabulary,word_vects,classes = parse_file("sms.text")
    print vocabulary
    print word_vects
    print classes
    dataset = []
    for word_vect in word_vects:
        doc_vect = get_doc_vector(word_vect,vocabulary)
        dataset.append(doc_vect)
    print dataset
    cond_probs,cls_probs = train(dataset,classes)
    print cond_probs
    print cls_probs

    #测试文本
    test_word_vect,cls =parse_line("love is weakness")
    test_word_data = get_doc_vector(test_word_vect,vocabulary)
    print test_word_data
    pred_cls = classify(test_word_data,cond_probs,cls_probs)
    print pred_cls

    chart_show(cond_probs,cls_probs)
