# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:50:09 2016

@author: blowv6
"""
import numpy
 
from sklearn.feature_extraction.text import CountVectorizer

input_fname = "result.txt"
output_vec_fname = "vectorization.txt"

with open("result.txt") as fr:
    raw_patent_data = fr.readlines()

#The patent_id and GranrtDate are not to be vectorized, named: not_vect.
#The name, location, citing and reference are to be vectorized, named: need_vect.
not_vect = [[],[]]
need_vect = [[],[],[],[]]

for line in raw_patent_data:
    line = line.strip()#delete the '\n'
    line = line.replace('nan','')
    line = line.replace('NULL','')
    line = line.replace('N/A', '')
    line = line.split('\t')
    #No and date
    not_vect[0].append(line[0])
    not_vect[1].append(line[1])
    # name; choose the first name
    names = str.split(line[2],'+')
    need_vect[0].append(names[0])
    # location
    for i in range(3,6):
        line[i] = str.split(line[i],'+')[0]
    location = ' '.join(line[3:6])
    need_vect[1].append(location)
    # citing
    citing = line[6].replace('+', ' ')
    need_vect[2].append(citing)
    # CPC
    cpc = line[7].replace('+', ' ')
    need_vect[3].append(cpc)
    
#extracting data finished
vectorizer = CountVectorizer(min_df=1)
vect = []
for i in range(0,4):
    X = vectorizer.fit_transform(need_vect[i])
    feature_vec = X.toarray()
    vect.append(feature_vec)

output_vect  = numpy.concatenate((vect[0],vect[1],vect[2],vect[3]),axis = 1)        
