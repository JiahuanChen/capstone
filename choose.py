# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:49:15 2016

@author: blowv6
"""
import numpy
import os
import os.path

from vectorization import vectorize

input_root = "test/"
output_root = "test_vect/vect"
count = 0;
for parent,dirnames,filenames in os.walk(input_root):
    for n in filenames:
        try:
            vec,d,e = vectorize(input_root + n)
            numpy.savetxt(output_root + n,X=vec[1],fmt = '%.0e')
            if not count%100:
                print(count*1./len(filenames))
            count += 1
        except:
            print(n)