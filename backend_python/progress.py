from methods import *
import time

time_start = time.time()

dataset = jsonConvert('newfile.json')
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

print 'YO\n\n'
print dictionary

#Calculate score
#print topMatches(dictionary, 'Hunan Wok Chinese Restaurant', n=10)

#example = 'Bellisario Pizza Shop'
#for i in dictionary:
#	value = supportVector(dictionary, i, example, lowerbound, upperbound)
#	if value > 0:
#		doRecommend.append(i)
#	elif value < 0:
#		dontRecommend.append(i)
#	else:
#		ambiguous.append(i)
#
#print 'Do Recommend: '
#for i in doRecommend:
#	print i
#print '\n\n'
#print 'Dont Recommend: '
#for i in dontRecommend:
#	print i
#print '\n\n'
#print 'Ambiguous: '
#for i in ambiguous:
#	print i
#print '\n\n'



#print "Tries: "
#print tries
#print "Entries: "
#print entries
#print '\nRuntime: ' + str(total_time)