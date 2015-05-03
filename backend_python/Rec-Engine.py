from methods import *
from dataprocess import *
import time

dataset = jsonConvert('datasets/subset_list.json')
dictionary = {}
topstars = {}

entries = 0
tries = 0
lowerbound = 0.5
upperbound = 0.8
doRecommend = []
dontRecommend = []
ambiguous = []


#Initialize dictionary
for i in dataset:
	if 'Ambience' in  i['attributes']:
		dictionary[i['name']] = i['attributes']['Ambience']
		topstars[i['name']]= [i['stars']]
		entries = entries + 1
	tries = tries + 1
print "Table Input: " + str(tries)
print "Valid Entries: " + str(entries)
print '\n'



#---------------------------------------------------------------

#top stars
print 'topstars results:'
time_start = time.time()
results = topStarRating(topstars,n=10)
print results
outputdata(dictionary,results, 'topstar')

time_end = time.time()
total_time = time_end - time_start
print 'Runtime: ' + str(total_time)
print'\n'

#euclidean
print 'euclidean distance results:'
time_start = time.time()
results = geteuclidean(dictionary, 'Taipei South', n=10)
print results
outputdata(dictionary,results, 'euclidean')

time_end = time.time()
total_time = time_end - time_start
print 'Runtime: ' + str(total_time)
print'\n'


#Pearson's corrolations 
print 'Pearson\'s corrolations results:'
time_start = time.time()
pearsons = topMatches(dictionary, 'Taipei South', n=10)
print pearsons 
outputdata(dictionary,results, 'pearsons')

time_end = time.time()
total_time = time_end - time_start
print 'Runtime: ' + str(total_time)
print'\n'


#Support Vector Strategy
print 'support vector results:'
time_start = time.time()
results = getSVM(dictionary, 'Taipei South', upperbound,lowerbound, n=10)
print results 
outputdata(dictionary,results, 'SVM')

time_end = time.time()
total_time = time_end - time_start
print 'Runtime: ' + str(total_time)
print'\n'


#-----------------------------------------?? those dont work
#Summation Strategy
print 'summation test'
print getSummationScore(dictionary, 'Taipei South', 'Cafe Zinho')
print getSharedCategories(dictionary, 'Taipei South', 'Cafe Zinho')
print'\n'

