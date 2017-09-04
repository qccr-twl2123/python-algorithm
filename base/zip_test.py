#!/usr/bin/python
import numpy as np
x = [1, 2, 3]

y = [4, 5, 6]

z = [7, 8, 9]

xyz = zip(x, y, z)

print xyz

x = [1, 2, 3]
y = [4, 5]
xy = zip(x, y)
print xy

x = [1, 2, 3]
x = zip(x)
print x


x = zip()
print x


x = [1, 0]
y = [1, 1, 0]
z = [1]

dataset = x+y+z
print  np.array(dataset)
classes =["spam","mmm","spam"]



print zip(dataset,classes)