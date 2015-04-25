import json;

data = []
with open('subset.json') as f:
    for line in f:
        data.append(json.loads(line))


print data