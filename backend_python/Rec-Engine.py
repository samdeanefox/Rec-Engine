from methods import *
from dataprocess import *
import time

time_start = time.time()

dataset = jsonConvert('datasets/subset_list.json')
dictionary = {}

entries = 0
tries = 0
lowerbound = 0.06
upperbound = 0.09
doRecommend = []
dontRecommend = []
ambiguous = []

time_end = time.time()
total_time = time_end - time_start

#Initialize dictionary
for i in dataset:
	if 'Ambience' in  i['attributes']:
		dictionary[i['name']] = i['attributes']['Ambience']
		entries = entries + 1
	tries = tries + 1

example = 'Bellisario Pizza Shop'
for i in dictionary:
	value = supportVector(dictionary, i, example, lowerbound, upperbound)
	if value > 0:
		doRecommend.append(i)
	elif value < 0:
		dontRecommend.append(i)
	else:
		ambiguous.append(i)
print 'Do Recommend: '
for i in doRecommend:
	print i
print '\n\n'
print 'Dont Recommend: '
for i in dontRecommend:
	print i
print '\n\n'
print 'Ambiguous: '
for i in ambiguous:
	print i
print '\n\n'

print "Tries: "
print tries
print "Entries: "
print entries
print '\nRuntime: ' + str(total_time)

#Support Vector Strategy
results = topMatches(dictionary, 'Taipei South', n=10)
print results 


#Summation Strategy
print getSummationScore(dictionary, 'Taipei South', 'Cafe Zinho')
print getSharedCategories(dictionary, 'Taipei South', 'Cafe Zinho')


#output result files from toMatch
outputdata(dictionary,results)
