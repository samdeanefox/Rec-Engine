import json
import csv

from math import sqrt

#Data-Handling Methods
def jsonConvert(file_descriptor):
	data = []
	with open(file_descriptor) as f:
	    for line in f:
	        data.append(json.loads(line))
	return data

def toJSON(dict_file):
	return json.dumps(dict_file, ensure_ascii=False)

def outputdata(dict_data,restaurant_list, filename):
	#resultdetails ={}	
	#for i in restaurant_list:
	#	resultdetails[i[0]] = dict_data[i[0]]
	
	with open("output/"+filename+".csv", "wb") as f:
    		writer = csv.writer(f)
		writer.writerow(['Top Pick', 'Best Scores'])
   		writer.writerows(restaurant_list)


# need one for to csv?
