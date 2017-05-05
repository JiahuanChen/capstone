#========= To remove repeated patent id =============
label_list = []
patent_id = []
assignee_name = []
with open("clus_result.txt","r") as infile:
	content = infile.readlines()

for i in range(len(content)):
	label_list.append(content[i].split('\t')[0])
	patent_id.append(content[i].split('\t')[1])
	assignee_name.append(content[i].split('\t')[2])

#==========No new label for now ========
with open("new_result1.txt","w") as outfile:
	label_check = []
	id_check = []
	name_check = []
	for i in range(len(content)):
		if patent_id[i] not in id_check:
			id_check.append(patent_id[i])
			outfile.write(content[i])
