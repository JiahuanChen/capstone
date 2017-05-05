#===== Label 

with open("Anew_result1.txt","r") as infile:
	content = infile.readlines()

patent_id = []
assignee_name = []
st_name = []
for i in range(len(content)):
	# label_list.append(content[i].split('\t')[0])
	patent_id.append(content[i].split('\t')[0])
	assignee_name.append(content[i].split('\t')[1])
	st_name.append(content[i].split('\t')[2].rstrip())

#==========No new label for now ========
st_dict = {}
st_name_check = []
group_id = -1
#========= Build a dictionary =======
for i in range(len(content)):
	if st_name[i] not in st_name_check:
		st_name_check.append(st_name[i])
		group_id += 1
		st_dict[st_name[i]] = group_id
		print(group_id)

#======== new file =====
with open("Afinal_result.txt","w") as outfile:
	for i in range(len(content)):
		outfile.write("Label_"+str(st_dict[st_name[i]])+"\t"+patent_id[i]+"\t"+assignee_name[i]+"\t"+st_name[i]+"\n")