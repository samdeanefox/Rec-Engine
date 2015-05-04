import json
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
	resultdetails ={}	
	for i in restaurant_list:
		resultdetails[i[0]] = dict_data[i[0]]

	fo = open("output/"+filename+".json", "wb")

# change just the score
	fo.write(toJSON(restaurant_list));


# need one for to csv?
