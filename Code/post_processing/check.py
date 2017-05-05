# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:45:39 2016

Check result

@author: blowv6
"""
import os

new_path = "../../data/Clus_fixed/"
old_path = "../../data/Clus/"
init = []
for parent,dirnames,filenames in os.walk(old_path):
    for i in dirnames:
        init.append(i)

for i in init:
    old_patent = {}
    new_patent = {}
    old_count = 0
    new_count = 0
    for parent,dirnames,filenames in os.walk(old_path+i+'/'):
        for n in filenames:
            with open(os.path.join(parent,n)) as f:
                lines = f.readlines()
            for line in lines:
                split_line = line.strip().split('\t')
                old_patent[split_line[1]] = 1
                old_count += 1

    for parent,dirnames,filenames in os.walk(new_path+i+'/'):
        for n in filenames:
            with open(os.path.join(parent,n)) as f:
                lines = f.readlines()
            for line in lines:
                split_line = line.strip().split('\t')
                new_patent[split_line[1]] = 1
                new_count += 1
    
    print(i)
    # new_count is the number of lines in fixed data
    print(len(old_patent) - len(new_patent),len(old_patent)-new_count)
            