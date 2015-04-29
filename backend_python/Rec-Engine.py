from methods import *
from dataprocess import *
import time

dataset = jsonConvert('datasets/subset_list.json')
dictionary = {}

entries = 0
tries = 0
lowerbound = 0.06
upperbound = 0.09
doRecommend = []
dontRecommend = []
ambiguous = []


#Initialize dictionary
for i in dataset:
	if 'Ambience' in  i['attributes']:
		dictionary[i['name']] = i['attributes']['Ambience']
		entries = entries + 1
	tries = tries + 1
print "Table Input: " + str(tries)
print "Valid Entries: " + str(entries)
print '\n'


## testing SVM methods... tbc
example = 'Bellisario Pizza Shop'
for i in dictionary:
	value = supportVector(dictionary, i, example, lowerbound, upperbound)
	if value > 0:
		doRecommend.append(i)
	elif value < 0:
		dontRecommend.append(i)
	else:
		ambiguous.append(i)

print 'Do Recommend:'
print '------------'
for i in doRecommend:
	print i
print '\n\n'

print 'Dont Recommend:'
print '------------'
for i in dontRecommend:
	print i
print '\n\n'

print 'Ambiguous:'
print '------------'
for i in ambiguous:
	print i
print '\n\n'



#---------------------------------------------------------------

#Pearson's corrolations 
print 'Pearson\'s corrolations results:'
time_start = time.time()
pearsons = topMatches(dictionary, 'Taipei South', n=10)
print pearsons 

time_end = time.time()
total_time = time_end - time_start
print 'Runtime: ' + str(total_time)
print'\n\n'



#Summation Strategy
print 'summation test'
print getSummationScore(dictionary, 'Taipei South', 'Cafe Zinho')
print getSharedCategories(dictionary, 'Taipei South', 'Cafe Zinho')

#Support Vector Strategy
print 'support vector results:'
time_start = time.time()
results = topMatches(dictionary, 'Taipei South', n=10)
print results 

time_end = time.time()
total_time = time_end - time_start
print 'Runtime: ' + str(total_time)


#------------------------------------------
#output result files from toMatch
outputdata(dictionary,pearsons, 'results')
