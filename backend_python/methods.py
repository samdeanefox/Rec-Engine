import json;

def jsonConvert(file_descriptor):
	data = []
	with open(file_descriptor) as f:
	    for line in f:
	        data.append(json.loads(line))
	return data