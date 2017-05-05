#!/usr/bin/env python

def extract_raw_output(path):
	'''
	File name: extract_raw_output.py
	Author: Zhechen Yan
	Date created: 10/15/2016
	Date last modified: 10/15/2016
	Python Version: 3.5.2
	Desc: given the path and fields of the raw tsv file, extract the corresponding filds from it and output as a txt file.
	input type:
	path : str
	fields : list of str
	output : .txt file
	'''
	__author__ = "Zhechen Yan"
	__copyright__ = "Copyright 2016, Fung institute of Engineering, UC Berkeley"
	__credits__ = ["Zhechen Yan", "Jiahuan Chen", "Liangjing Zhu",
						"Guancheng Li", "Lee Fleming"]
	__version__ = "0.0.1"
	__maintainer__ = "Zhechen Yan"
	__email__ = "harry.yan@berkeley.edu"
	__status__ = "Research"

	import pandas as pd
	with open('./data/no.match.txt','w') as fn:
		pass
	with open('./data/result.txt','w') as fr:
		pass
	with open('./data/double.check.txt','w') as fe:
		pass
	with open('./data/perior2006.txt','w') as fp:
		pass

	df = pd.read_csv(path, sep = '\t', error_bad_lines = False)
	with open('./data/patent.id.txt', 'r') as f:
		patent_id_list = f.readlines()
		i=1
		for patent_id in patent_id_list:
			patent_id = patent_id.strip()
			# int str format
			# if patent_id.isdigit() == True:
			# 	patent_id = int(patent_id)
			print(i)
			i += 1
			try:
				if patent_id.isdigit() == True:
					x = df[df.PatentNo==int(patent_id)].index
				else:
					x = df[df.PatentNo==patent_id].index
				index = int(str(df.ix[x].PatentNo).split()[0])
				with open('./data/result.txt','a') as fr:
					# Check the Year

					if df.ix[index].GrantDate[0:4].isdigit() == False or int(df.ix[index].GrantDate[0:4]) < 2006:
						with open('./data/no.match.txt','a') as fn:
							fn.writelines(patent_id+'\n')
						continue
					# Check if there is 'nan' in any of these fields
					checklist=[]
					checklist.append(str(df.ix[index].PatentNo))
					checklist.append(str(df.ix[index].GrantDate))
					checklist.append(str(df.ix[index].AssigneeName))
					checklist.append(str(df.ix[index].AssigneeCountryCode))
					checklist.append(str(df.ix[index].AssigneeStateCode))
					checklist.append(str(df.ix[index].AssigneeCityCode))
					checklist.append(str(df.ix[index].Reference))
					checklist.append(str(df.ix[index].CPCClass))
					if 'nan' in checklist:
						with open('./data/double.check.txt','a') as fd:
							fd.writelines(patent_id+'\t'+str(checklist.index('nan'))+'\n')

					# write into file: result.txt
					fr.writelines(str(df.ix[index].PatentNo)+'\t')
					fr.writelines(str(df.ix[index].GrantDate)+'\t')
					fr.writelines(str(df.ix[index].AssigneeName)+'\t')
					fr.writelines(str(df.ix[index].AssigneeCountryCode)+'\t')
					fr.writelines(str(df.ix[index].AssigneeStateCode)+'\t')
					fr.writelines(str(df.ix[index].AssigneeCityCode)+'\t')
					fr.writelines(str(df.ix[index].Reference)+'\t')
					if str(df.ix[index].CPCClass) != 'nan':
						fr.writelines(str(df.ix[index].CPCClass[0:4])+'\n')
					else:
						fr.writelines(str(df.ix[index].CPCClass)+'\n')
			except ValueError:
				x = df[df.PatentNo==patent_id].index
				index = int(str(df.ix[x].PatentNo).split()[0])
				with open('./data/result.txt','a') as fr:
					# Check the Year
					if df.ix[index].GrantDate[0:4].isdigit() == False or int(df.ix[index].GrantDate[0:4]) < 2006:
						with open('./data/no.match.txt','a') as fn:
							fn.writelines(patent_id+'\n')
						continue
					# Check if there is 'nan' in any of these fields
					checklist=[]
					checklist.append(str(df.ix[index].PatentNo))
					checklist.append(str(df.ix[index].GrantDate))
					checklist.append(str(df.ix[index].AssigneeName))
					checklist.append(str(df.ix[index].AssigneeCountryCode))
					checklist.append(str(df.ix[index].AssigneeStateCode))
					checklist.append(str(df.ix[index].AssigneeCityCode))
					checklist.append(str(df.ix[index].Reference))
					checklist.append(str(df.ix[index].CPCClass))
					if 'nan' in checklist:
						with open('./data/double.check.txt','a') as fd:
							fd.writelines(patent_id+'\t'+str(checklist.index('nan'))+'\n')

					# write into file: result.txt
					fr.writelines(str(df.ix[index].PatentNo)+'\t')
					fr.writelines(str(df.ix[index].GrantDate)+'\t')
					fr.writelines(str(df.ix[index].AssigneeName)+'\t')
					fr.writelines(str(df.ix[index].AssigneeCountryCode)+'\t')
					fr.writelines(str(df.ix[index].AssigneeStateCode)+'\t')
					fr.writelines(str(df.ix[index].AssigneeCityCode)+'\t')
					fr.writelines(str(df.ix[index].Reference)+'\t')
					if str(df.ix[index].CPCClass) != 'nan':
						fr.writelines(str(df.ix[index].CPCClass[0:4])+'\n')
					else:
						fr.writelines(str(df.ix[index].CPCClass)+'\n')
						

extract_raw_output('./data/records_0714.tsv')
