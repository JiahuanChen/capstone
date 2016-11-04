# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:50:09 2016

@author: blowv6

Usage:

from vectorization import vectorize
vector = vectorize(input_fname = "*.txt" )


input: patent data(txt file)
output: contant the following 2 part:
        vector[0]: 3 lists of 0: PatentNo., 1: Date, 2: Assignee name
        vector[1]: vector array
input data format:
[0]ID [1]Assignee_name [2]date [3,4,5]location [6]citation [7]CPC 
"""
import numpy
 
from sklearn.feature_extraction.text import CountVectorizer

def vectorize(input_fname = "result.txt", array_tpye = "int8"):
    with open(input_fname) as fr:
        raw_patent_data = fr.readlines()
    
    #The patent_id and GranrtDate are not to be vectorized, named: not_vect.
    #The name, location, citing and reference are to be vectorized, 
    #named: need_vect.
    not_vect = [[],[],[]] #ID,name,date
    need_vect = [[],[],[],[],[]] #
    for line in raw_patent_data:
        line = line.strip()#delete the '\n'
        line = line.replace('nan','')
        line = line.replace('NULL','')
        line = line.replace('N/A', '')
        line = line.split('\t')
        #ID and data,[0,2]
        not_vect[0].append(line[0])
        not_vect[1].append(line[2])
        #Name[1]; choose the first assignee name
        names = str.split(line[1],'+')
        not_vect[2].append(names[0])
        need_vect[0].append(names[0])
        #Location[3-5]; choose the first assignee location
        for i in range(3,6):
            line[i] = str.split(line[i],'+')[0]
        location = ' '.join(line[3:6])
        need_vect[1].append(location)
        #Citing[6]
        citing = line[6].replace('+', ' ')
        need_vect[2].append(citing)
        #CPC[7]
        cpc = line[7].replace('+', ' ')
        need_vect[3].append(cpc)
        #Inventor[8], "+": different inventors, ";": different names
        #last name1;first name1+last name2;first name2...
        inventor = line[8].replace('; ', '')
        inventor = inventor.replace('+', ' ')
        need_vect[4].append(inventor)
    #Extracting data finished
    
    #Vectorize 5 attributes respectively
    vectorizer = CountVectorizer(dtype = array_tpye,token_pattern='\\b\\w+\\b')
    vect = []
    words_in_bag = []
    for i in range(0,5):
        empty = False;
        #check if this string is empty, like "  " or " "
        for item in need_vect[i]:
            if len(item.replace(' ','')) == 0:
                empty = True
                break
        if not empty:
            X = vectorizer.fit_transform(need_vect[i])
            feature_vec = X.toarray()
            vect.append(feature_vec)
            words_in_bag.append(vectorizer.get_feature_names())
            
    #Merge four vectors into a single array
    vecterized = vect[0];
    for i in range(1,len(vect)):
        vecterized  = numpy.concatenate((vecterized,vect[i]),axis = 1)
   #Merge unvectorized data and vector array
    output = [] 
    output.append(not_vect)
    output.append(vecterized)
    return output,vect,not_vect,need_vect,words_in_bag
