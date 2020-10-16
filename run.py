import json
import os
import operator
from collections import OrderedDict
import re
#import statistics 

# Load from JSON file
f = open('json_file.txt', 'r')
items = json.loads(f.read())

# Parsing and ordering.
sorted_items = dict()
for item in items:
    _id = int(re.findall(r'\d+', item['image_id'])[0])
    sorted_items[_id] = float(item['mean_score_prediction'])

#avg_value = statistics.mean(sorted_items.values())
#print(avg_value)

good_idx = set()
last_good_key = 0
temp_idx = dict()
for key, value in sorted_items.items():
    #print key
    if value > 5.3:
        temp_idx[key] = value
        if key > last_good_key + 30:
             #good_idx.add(max(temp_idx.items(), key=operator.itemgetter(1))[0])
             good_idx.add(max(temp_idx.items(), key=lambda k: k[1])[0])
             temp_idx = dict()
        last_good_key = key
print(good_idx)

#for key, value in sorted_items.items():
#    if key not in good_idx:
#        os.remove('frames/out-'+str(key)+'.jpg')
