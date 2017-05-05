# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:15:05 2016

@author: blowv6
"""
import time

input_path = "../../test5_1107/new_result1.txt"
output_path = "../../test5_1107/new_result1_labeled.txt"

with open(input_path) as fr:
    lines = fr.readlines()
    
new_lines = []
names = {};
for line in lines:
    #separate the line(string) into list,new label index is [3]
    line = line.strip()
    line = line.split('\t')
    #if not found in dictionary, add it
    if not names.get(line[3]):
        names[line[3]] = len(names)
    #add label number to the end
    line.append(str(names.get(line[3])))
    new_line = ""
    #merge the list into string
    for i in range(len(line)):
        new_line += line[i]
        new_line += '\t'
    new_line = new_line[:-1]+'\n'
    new_lines.append(new_line)

with open(output_path,"w") as fr:
    fr.write(time.strftime('%Y-%m-%d,%H:%m',time.localtime()))
    fr.write('\n')
    fr.writelines(new_lines) 
    