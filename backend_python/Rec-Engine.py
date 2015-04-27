from methods import *
import time

time_start = time.time()

dataset = jsonConvert('newfile.json')
dictionary = {}
resultdetails ={}

entries = 0
tries = 0

time_end = time.time()
total_time = time_end - time_start

#Initialize dictionary
for i in dataset:
	if 'Ambience' in  i['attributes']:
		dictionary[i['name']] = i['attributes']['Ambience']
		entries = entries + 1
	tries = tries + 1

#Calculate score
results = topMatches(dictionary, 'Taipei South', n=10)
print results 


#output result files
for i in results:
	resultdetails[i[0]] = dictionary[i[0]]

fo = open("results.json", "wb")
fo.write(toJSON(resultdetails));


print "Tries: "
print tries
print "Entries: "
print entries
print '\nRuntime: ' + str(total_time)