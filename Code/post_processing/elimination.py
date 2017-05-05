# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:48:37 2016

@author: blowv6

Post-process.
Eliminate the over-splitted patents.
steps:
    1. find over-lapped patents
    2. choose a best-fit bucket(the smallest distance unless 0)
    3. delete from other buckets
Output:
    cluster files that are changed
    
*Deal with all data at once. May have memory problem
"""

import os
import os.path
from sklearn.cluster import KMeans
import numpy
import time

from vectorization_nospace import vectorize

start = time.clock()
label_path = "../../data/Clus/"

#load labeled imfromation

#record block path
input_subpath = []
for (dirpath, dirnames, filenames) in os.walk(label_path):
    for n in dirnames:
        p = os.path.join(dirpath,n)
        input_subpath.append(p)

#patent ID(string): files path(list)
over_lap = {}

#file(string):number of clusters(int)
clusters = {}

#iterate each Block(A,B,C,...)
for i in input_subpath:
    count = 0
    patent_id = {}
    #record patent IDs, and find duplicate patents
    for (dirpath, dirnames, filenames) in os.walk(i):
        for n in filenames:
            #string:string
            p = os.path.join(dirpath,n)
            with open(p) as f:
                lines = f.readlines()
            max_cluster = 1
            for l in lines:
                # format: label, patent ID, name
                l = l.strip().split('\t')
                max_cluster = max(max_cluster,int(l[0])+1)
                clusters[p.split("Clus")[1].split("\\")[1]] = max_cluster
                if l[1] not in patent_id:
                    patent_id[l[1]] = p.split("Clus")[1].split("\\")[1]
                else:
                    # this patent is overlapped with and previous one
                    # if it is has not been recorded, add previous
                    # then, update the record
                    if l[1] not in over_lap:
                        over_lap[l[1]] = [patent_id[l[1]]]
                    over_lap[l[1]].append(p.split("Clus")[1].split("\\")[1])
        
            #show progress
            if not count%100:
                print(dirpath[-1], count*1./len(filenames))
            count += 1
# all the duplicate patents are recond in over_lap

#for each patents, estimate the distance in different buckets,
#and then choose the best-fitted one
raw_path = "../../data/data_initial_letter/"
count  = 0
fixed = {}
for patent in over_lap:
    if not count%10:
        print(count*1./len(over_lap))
    count += 1
    distance = []
    for fn in over_lap[patent]:
        #find the index in raw data
        raw_filename = raw_path+fn[0]+'/'+fn+'.txt'
        #vecterize the file
        vec = vectorize(raw_filename)
        if vec != 0:
            vec = vec[0]
            with open(raw_filename,encoding='utf-8') as f: 
                lines = f.readlines()
            #find the index of the overlapped patent(i)
            i = 0
            for line in lines:
                line = line.strip().split('\t')
                if patent == line[0]:
                    break
                i += 1
            #vector without the overlap patent
            overlap_vec = vec[i]
            overlap_vec = overlap_vec.reshape(1,-1)
            #cluster the vector
            kmeans = KMeans(n_clusters=clusters[fn]).fit(vec)
            #get the score between each cluster and the overlapped vector
            score = kmeans.transform(overlap_vec)
            m = max(score[0])
            #find the minimum
            for i in range(0,score.size):
                #if score is 0, it means it is the only element in this cluster.
                if score[0][i] != 0:
                    m = min(m,score[0][i])
            distance.append(m)
    # updata the fixed data
    if len(distance) != 0:
        min_dis = min(distance)
        for i in range(len(distance)):
            if min_dis == distance[i]:
                break
        fixed[patent] = over_lap[patent][i]
    else:
        fixed[patent] = over_lap[patent][0]

#update label
fixed_label_path = "../../data/fixed_label/"
if not os.path.exists(fixed_label_path):
    os.makedirs(fixed_label_path)

count = 0
for patent in fixed:
    if not count%10:
        print(count*1./len(fixed))
    count += 1
    for fn in over_lap[patent]:
        # if the patent does not belongs to this bucket, delete it
        if fn != fixed[patent]:
            # if fixed file exit, read the exit file, else, read original file
            if os.path.exists(fixed_label_path+fn[0]+'/'+fn+'Clus.txt'):
                with open(fixed_label_path+fn[0]+'/'+fn+'Clus.txt') as f:
                    lines = f.readlines()
            else:
                with open(label_path+fn[0]+'/'+fn+'Clus.txt','r') as f:
                    lines = f.readlines()
            new_lines = []
            for line in lines:
                split_line = line.strip().split('\t')
                # if is not the patent, copy it to new_lines
                if split_line[1] != patent:
                    new_lines.append(line)
            fixed_label_subpath = fixed_label_path+fn[0]+'/'
            if not os.path.exists(fixed_label_subpath):
                os.makedirs(fixed_label_subpath)
            with open(fixed_label_subpath+fn+'Clus.txt','w') as f:
                f.writelines(new_lines)
                

end = time.clock()
computing_time = end - start