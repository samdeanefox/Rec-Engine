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



#Similarity Evaluation Methods
def getPearsonScore(dict,r1,r2):
 
  si={}
  for item in dict[r1]:
    if item in dict[r2]: si[item]=1
  
  n=len(si)
  
  if n==0: return 0

  sum1=sum([dict[r1][it] for it in si])
  sum2=sum([dict[r2][it] for it in si])
  
  sum1Sq=sum([pow(dict[r1][it]+1,2) for it in si])
  sum2Sq=sum([pow(dict[r2][it]+1,2) for it in si])
  
  pSum=sum([dict[r1][it]*dict[r2][it] for it in si])

  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r

def getSharedCategories(dict, r1, r2):

  categories = []

  for item1 in dict[r1]:
    for item2 in dict[r2]:
      if item1 == item2:
        if dict[r1][item1] == dict[r2][item2] == 1:
          #If both == 1, weight higher than both == 0
          categories.append(item1)
  return categories

def getSummationScore(dict, r1, r2):

  similarities = 0

  for item1 in dict[r1]:
    for item2 in dict[r2]:
      if item1 == item2:
        if dict[r1][item1] == dict[r2][item2] == 1:
          #If both == 1, weight higher than both == 0
          similarities = similarities + 5
        elif dict[r1][item1] == dict[r2][item2] == 0:
          similarities = similarities + 1
  return similarities


#Output Methods
def topMatches(dict,person,n=5,similarityFunction=getPearsonScore):
	scores=[(other,similarityFunction(dict,person,other))
                       for other in dict if other!=person]
  	scores.sort(key=lambda x: x[1])
  	scores.reverse()
  	return scores[0:n]

def supportVector(dict, restaurant, comparator, lowerbound, upperbound, similarityFunction=getPearsonScore):
  val = similarityFunction(dict, restaurant, comparator)
  if val > upperbound:
    return 1
  if val < lowerbound:
    return -1
  return 0


#def topStarRating():
