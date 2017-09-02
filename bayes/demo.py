#!/usr/bin/python
import collections

list = ["asa","mmm","dadsa"];
doc_vect =[0] * len(list)
print doc_vect




s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
print(d)

sub_datasets = collections.defaultdict(lambda :[]);

for i in range(1,10):
   sub_datasets["ad"].append(10)

print  sub_datasets
