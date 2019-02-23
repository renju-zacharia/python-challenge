# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 07:05:46 2019

@author: RZ0001
"""

d = {}

d['name'] = 'renju'
d['num'] = '123'

print (d)

x = 'age'

if x in d:
    print("yes")
else:
    d[x] = 32
    print("no")    
    
print (d)

d[x] = d[x] + 1

print(d)