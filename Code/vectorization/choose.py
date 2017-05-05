# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:49:15 2016

@author: blowv6

Usage:
input_path: the patent data path
output_path: the patent data path and prefix
e.g. input_path = "test/test.txt" output_path = "test_vect/vectest.txt" 

Check the paths and the files in those paths!!!
This script will vectorize all the files in input path!!!
"""
import numpy
import time
import os
import os.path

from vectorization import vectorize

# Add your input and output path.
input_path = "../../test7_1118/"
output_path = "../../test7_1118/vec/"
#input_path = "test/"
#output_path = "test_vect/"
error = []
if not os.path.exists(output_path):
    os.makedirs(output_path)
skip_list = []
count = 0;
chosen_feature=("name","location","cpc","inventor","examiner")
for parent,dirnames,filenames in os.walk(input_path):
    for n in filenames:
        try:
            vec = vectorize(input_path + n,feature=chosen_feature)
            if vec:
                numpy.savetxt(output_path + n[0:-4]+'vec'+n[-4:],X=vec[0],fmt = '%.0e')
            else:
                skip_list.append(n+'\n')
# show the progress
            if not count%100:
                print(count*1./len(filenames))
            count += 1
        except:
            # print failed file name
            print(n)
            error.append(n)

with open(output_path+"skip.txt","w") as fr:
    fr.write(time.strftime('%Y-%m-%d,%H:%m',time.localtime()))
    fr.write('\n')
    fr.writelines(skip_list)

with open(output_path+"errors.txt","w") as fr:
    fr.writelines(error)
    