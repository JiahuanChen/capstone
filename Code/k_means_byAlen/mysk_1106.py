#### Find the cluster numbers k before clustering
from sklearn.cluster import KMeans
#from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import argparse
import os
import os.path


###########
# READ ME #
###########
# ============ Just for Astr80 for now=======
input_path1 = "./A/"
input_path2 = "./Avec/"
output_path = "./AClus/"
# #==============Command Example: Python mysk.py --start 1 --end 6 --interval 1
# parser = argparse.ArgumentParser(description="Find the rough cluster numbers")
# parser.add_argument('--infile',dest="infile",help="Sepcify the file name to cluster")
# args = parser.parse_args()
#================Find the total distances under different cluster numbers=============
def total_distances(X,end):
	total_distances = []
	for i in range(1,end,1):
		kmeans = KMeans(n_clusters = i).fit(X)      	# Cluster under cluster numbers i
		total_distances.append(kmeans.inertia_)    		# Caculate the sum of samples' distance to cluster center
	return total_distances

#==============Find the number with the largest ratio===========
def k_find(dis_list):
	ratios = []                                    		# A list to store the ratio of two adjacent numbers
	print(dis_list)
	for i in range(len(dis_list)-1):
		if dis_list[i+1] != 0:							# This condition is to remove the cluster numbers with total diatance = 0
			ratios.append(dis_list[i]/dis_list[i+1])
		else:
			ratios.append(1)
	if len(ratios) <= 1:
		k_index = 1
	else:
		k_index = ratios.index(max(ratios))+1          		# Find the largest ratio and corresponding index in the total distances list
	return k_index 
#============== Cluster and Label accoring to original txt file and vector txt file ============
def Clustering(input_path1,input_path2,output_path,file_original,file_vector,file_Clustered):
	X = np.loadtxt(fname=(input_path2+file_vector),dtype="int8")		# Load vector file
	group_len = len(X)									# The length of vectors
	Y = total_distances(X,int(group_len*0.8))			# Assume at most (group_len*0.5) clusters in a group
	k_cluster = k_find(Y) + 1							# Cluster numbers in a group
	kmeans_final = KMeans(n_clusters=k_cluster).fit(X)  # Cluster under number k_cluster
	label_list = kmeans_final.labels_ 					# Label list
	with open((input_path1+file_original),"r") as infile:
		patent_assignee = infile.readlines()
		patent_id = []
		assignee_name = []
		for i in range(len(patent_assignee)):
			patent_id.append(patent_assignee[i].split('\t')[0])
			assignee_name.append(patent_assignee[i].split('\t')[1])
	#=========== Output lable index, patent id, assignee name in the clustered file ============ 
	label_index = os.path.splitext(file_original)[0]		# Label index for different file, this is for final files merging
	print(label_index)
	with open((output_path+file_Clustered),"w") as fw:
		for i in range(group_len):
			fw.write(str(label_index)+"_"+str(label_list[i])+"\t"+str(patent_id[i])+"\t"+str(assignee_name[i])+"\n")
	return
#=============== For files no need to cluster ==================
def Copy_noclus_file(input_path1,output_path,file_original,file_Clustered):
	with open((input_path1+file_original),"r") as infile:
		patent_assignee = infile.readlines()
		patent_id = []
		assignee_name = []
		for i in range(len(patent_assignee)):
			patent_id.append(patent_assignee[i].split('\t')[0])
			assignee_name.append(patent_assignee[i].split('\t')[1])
	#=========== Output lable index, patent id, assignee name in the clustered file ============ 
	label_index = os.path.splitext(file_original)[0]		# Label index for different file, this is for final files merging
	print(label_index)
	group_len = len(assignee_name)
	with open((output_path+file_Clustered),"w") as fw:
		for i in range(group_len):
			fw.write(str(label_index)+"\t"+str(patent_id[i])+"\t"+str(assignee_name[i])+"\n")
	return

def find_filelist(input_path):
	filelist = []
	for (dirpath, dirnames, filenames) in os.walk(input_path):
		for fn in filenames:
			if fn[0] != "." :								# This is to ignore hidden files
				filelist.append(fn)
	return filelist


filelist1 = find_filelist(input_path1)			# original txt file list
filelist2 = find_filelist(input_path2)			# vectors txt file list
for i in range(len(filelist1)):
	vec_file = os.path.splitext(filelist1[i])[0] + "vec.txt"
	clus_file = os.path.splitext(filelist1[i])[0] + "Clus.txt"
	if vec_file in filelist2:									# Find a corresponding vector file in filelist2
		Clustering(input_path1,input_path2,output_path,filelist1[i],vec_file,clus_file)
	elif vec_file not in filelist2:
		Copy_noclus_file(input_path1,output_path,filelist1[i],clus_file)



# #X=np.loadtxt(fname=(args.infile[0]+"vec.txt"),dtype="int8")
# X=np.loadtxt(fname=(os.path.splitext(args.infile)[0]+"vec.txt"),dtype="int8")
# group_len= len(X)
# Y=total_distances(X,group_len)
# k_cluster = k_find(Y) + 1                        		# Find the cluster numbers k
# print ("The numbers of expexted clusters:")
# print (k_cluster)
# kmeans_final = KMeans(n_clusters=k_cluster).fit(X) 		# Cluster under cluster numbers k
# label_list = kmeans_final.labels_
# with open(args.infile,'r') as infile:
# 	patent_assignee = infile.readlines()
# 	patent_id = []
# 	assignee_name = []
# 	for i in range(len(patent_assignee)):
# 		patent_id.append(patent_assignee[i].split('\t')[0])
# 		assignee_name.append(patent_assignee[i].split('\t')[1])
# #============ Add label to each patent =============
# with open((os.path.splitext(args.infile)[0]+'Clustered.txt'),'w') as outfile:
# 	for i in range(group_len):
# 		outfile.write(str(label_list[i])+"\t"+str(patent_id[i])+"\t"+str(assignee_name[i])+"\n")



