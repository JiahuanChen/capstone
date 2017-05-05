# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:49:15 2016

@author: blowv6

Usage:
input_path: the patent data path
output_path: the patent data path and prefix
e.g. input_path = "test/test.txt" output_path = "test_vect/vectest.txt" 

Check the paths and the files in those paths!!!
You need to create the output path before running the script.
This script will vectorize all the files in input path!!!
"""
import numpy
import os
import os.path

from vectorization import vectorize

# Add your input and output path.
input_path = "../../test2_1103/A90/"
output_path = "../../test2_1103/A90vec/vec"

count = 0;
for parent,dirnames,filenames in os.walk(input_path):
    for n in filenames:
        try:
            vec = vectorize(input_path + n)
            numpy.savetxt(output_path + n,X=vec[0],fmt = '%.0e')
# show the progress
            if not count%100:
                print(count*1./len(filenames))
            count += 1
        except:
            # print failed file name
            print(n)