import json
from math import sqrt

def jsonConvert(file_descriptor):
	data = []
	with open(file_descriptor) as f:
	    for line in f:
	        data.append(json.loads(line))
	return data

def getScore(dict,p1,p2):
 
  si={}
  for item in dict[p1]:
    if item in dict[p2]: si[item]=1
  
  n=len(si)
  
  if n==0: return 0
  
  sum1=sum([dict[p1][it] for it in si])
  sum2=sum([dict[p2][it] for it in si])
  
  sum1Sq=sum([pow(dict[p1][it]+1,2) for it in si])
  sum2Sq=sum([pow(dict[p2][it]+1,2) for it in si])
  
  pSum=sum([dict[p1][it]*dict[p2][it] for it in si])

  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r

def topMatches(dict,person,n=5,similarity=getScore):
	scores=[(similarity(dict,person,other),other)
                       for other in dict if other!=person]
  	scores.sort()
  	scores.reverse()
  	return scores[0:n]