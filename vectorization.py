# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:50:09 2016

@author: blowv6

Usage:

from vectorization import vectorization
vector = vectorization(input_fname = "*.txt" )


input: patent data(txt file)
output: contant the following 2 part:
        vector[0]: 3 lists of 0: PatentNo., 1: Date, 2: Assignee name
        vector[1]: vector array
"""
import numpy
 
from sklearn.feature_extraction.text import CountVectorizer

def vectorize(input_fname = "result.txt", array_tpye = "int8"):
    with open(input_fname) as fr:
        raw_patent_data = fr.readlines()
    
    #The patent_id and GranrtDate are not to be vectorized, named: not_vect.
    #The name, location, citing and reference are to be vectorized, 
    #named: need_vect.
    not_vect = [[],[],[]]
    need_vect = [[],[],[],[]]
    
    count = 0
    for line in raw_patent_data:
        count += 1
        if count > 200:
            break
        line = line.strip()#delete the '\n'
        line = line.replace('nan','')
        line = line.replace('NULL','')
        line = line.replace('N/A', '')
        line = line.split('\t')
        #No and data
        not_vect[0].append(line[0])
        not_vect[1].append(line[1])
        #Name; choose the first assignee name
        names = str.split(line[2],'+')
        not_vect[2].append(names[0])
        need_vect[0].append(names[0])
        #Location; choose the first assignee location
        for i in range(3,6):
            line[i] = str.split(line[i],'+')[0]
        location = ' '.join(line[3:6])
        need_vect[1].append(location)
        #Citing
        citing = line[6].replace('+', ' ')
        need_vect[2].append(citing)
        #CPC
        cpc = line[7].replace('+', ' ')
        need_vect[3].append(cpc)
    #Extracting data finished.
    
    #Vectorize 4 attributes respectively
    vectorizer = CountVectorizer(min_df=1,dtype = array_tpye)
    vect = []
    for i in range(0,4):
        X = vectorizer.fit_transform(need_vect[i])
        feature_vec = X.toarray()
        vect.append(feature_vec)
    
    vecterized  = numpy.concatenate((vect[0],vect[1],vect[2],vect[3]), \
                                     axis = 1)    
    output = [] 
    output.append(not_vect)
    output.append(vecterized)
    return output