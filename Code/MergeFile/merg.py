# import glob

# read_files = glob.glob("*.txt")

# with open("result.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())
import os
import os.path

input_path  = "./AClus_standard/"

filelist = []
for (dirpath, dirnames, filenames) in os.walk(input_path):
	for fn in filenames:
		if fn[0] != "." :
			filelist.append(fn)


with open('result.txt', 'w') as outfile:
    for fname in filelist:
        with open(input_path+fname) as infile:
            for line in infile:
                outfile.write(line)

# with open("result.txt","w") as outfile:
# 	group_num = 0
# 	for i in range(len(filelist)):
# 		with open(filelist[i],"r") as infile:
# 			content = infile.read_files()
# 			lab_list=[]
# 			for j in range(len(content)):
# 				if content[j].split("\t")[0] not in lab_list:
# 				assignee_name.append(patent_assignee[i].split('\t')[1])


