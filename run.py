import json
import os
import re
import numpy as np

#SCORE_BIAS = -0.55
SCORE_BIAS = 0
FRAMES_GAP = 30

# Load from JSON file
f = open('input.json', 'r')
items = json.loads(f.read())

# Parsing and ordering.
sorted_items = dict()
for item in items:
    _id = int(re.findall(r'\d+', item['image_id'])[0])
    sorted_items[_id] = float(item['mean_score_prediction'])

#avg_value = sum(sorted_items.values()) / len(sorted_items.values())
#print(avg_value)
#print(max(sorted_items.values())) * 0.25

good_idx = set()
last_good_key = 0
temp_idx = dict()
for key, value in sorted_items.items():
    #if value > avg_value - SCORE_BIAS:
    if value > np.percentile(sorted_items.values(), 70):
        temp_idx[key] = value
        if key > last_good_key + FRAMES_GAP:
            good_idx.add(max(temp_idx.items(), key=lambda k: k[1])[0])
            temp_idx = dict()
        last_good_key = key
print(good_idx)

for key, value in sorted_items.items():
    if key not in good_idx:
        try:
            #print 'ok'
            os.remove('frames/out-'+str(key)+'.jpg')
            pass
        except Exception:
            pass
