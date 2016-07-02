# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 17:54:01 2016

@author: w7
"""

import csv
import numpy as np
from sklearn.svm import SVR

f = open('train.csv','rb')
reader = csv.reader(f)
ind = [] 
content = []
Length = []
clf = SVR(C=1.0,epsilon=0.2)

for line in reader:
    ind.append(line[0])
    content.append(line[1])
ind = ind[1:];
content = content[1:]
f.close()

Num = len(content)
for i in range(Num):
    Length.append(len(content[i]))

Input_data = []
Output_data = []
for i in range(1):
    in_tmp = content[i][:Length[i]]
    out_tmp = content[i][-1]
    #Input_data.append(in_tmp.split(',')
    #Output_data.append(out_tmp.split(',')
    
#Input_data = np.array(Input_data)
#Output_data = np.array(Output_data)

#clf.fit(Input_data[0],Output_data[0])