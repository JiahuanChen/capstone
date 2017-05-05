#### Find the cluster numbers k before clustering
from sklearn.cluster import KMeans
#from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import argparse
import os

###########
# READ ME #
###########

#==============Command Example: Python mysk.py --start 1 --end 6 --interval 1
parser = argparse.ArgumentParser(description="Find the rough cluster numbers")
# parser.add_argument('--start', dest='start', type=int, default=0, help='Specify where to start the scan')
# parser.add_argument('--end', dest='end', type=int, default=0, help='Specify where to end the scan')
# parser.add_argument('--interval', dest='interval', type=int, default=1000, help='Sepcify the interval')
parser.add_argument('--infile',dest="infile",help="Sepcify the file name to cluster")
args = parser.parse_args()


#================Find the total distances under different cluster numbers=============
# def total_distances(start,end,interval):
# 	total_distances = []
# 	for i in range(start,end,interval):
# 		kmeans = KMeans(n_clusters = i).fit(X)      	# Cluster under cluster numbers i
# 		total_distances.append(kmeans.inertia_)    		# Caculate the sum of samples' distance to cluster center
# 	return total_distances
def total_distances(X,end):
	total_distances = []
	for i in range(1,end,1):
		kmeans = KMeans(n_clusters = i).fit(X)      	# Cluster under cluster numbers i
		total_distances.append(kmeans.inertia_)    		# Caculate the sum of samples' distance to cluster center
	return total_distances

#==============Find the number with the largest ratio===========
def k_find(dis_list):
	ratios = []                                    		# A list to store the ratio of two adjacent numbers
	for i in range(len(dis_list)-1):
		if dis_list[i+1] != 0:							# This condition is to remove the cluster numbers with total diatance = 0
			ratios.append(dis_list[i]/dis_list[i+1])
	k_index = ratios.index(max(ratios))+1          		# Find the largest ratio and corresponding index in the total distances list
	return k_index 

#X=np.loadtxt(fname=(args.infile[0]+"vec.txt"),dtype="int8")
X=np.loadtxt(fname=(os.path.splitext(args.infile)[0]+"vec.txt"),dtype="int8")

group_len= len(X)

# Y=total_distances(args.start, args.end, args.interval)
Y=total_distances(X,group_len)
k_cluster = k_find(Y) + 1                        		# Find the cluster numbers k

print ("The numbers of expexted clusters:")
print (k_cluster)
kmeans_final = KMeans(n_clusters=k_cluster).fit(X) 		# Cluster under cluster numbers k

# print ("Labels of samples:")
label_list = kmeans_final.labels_
# print (label_list)                        		# Label each vector
# print "Cluster centers' point:"
# print kmeans_final.cluster_centers_				   		# Find the center of each cluster


with open(args.infile,'r') as infile:
	patent_assignee = infile.readlines()
	patent_id = []
	assignee_name = []
	for i in range(len(patent_assignee)):
		patent_id.append(patent_assignee[i].split('\t')[0])
		assignee_name.append(patent_assignee[i].split('\t')[1])

#============ Add label to each patent =============
with open((os.path.splitext(args.infile)[0]+'Clustered.txt'),'w') as outfile:
	for i in range(group_len):
		outfile.write("Label_"+str(label_list[i])+"\t"+str(patent_id[i])+"\t"+str(assignee_name[i])+"\n")



