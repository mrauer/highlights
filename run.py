import json
import os
import re

SCORE_BIAS = -0.65
FRAMES_GAP = 17

# Load from JSON file
f = open('input.json', 'r')
items = json.loads(f.read())

# Parsing and ordering.
sorted_items = dict()
for item in items:
    _id = int(re.findall(r'\d+', item['image_id'])[0])
    sorted_items[_id] = float(item['mean_score_prediction'])

avg_value = sum(sorted_items.values()) / len(sorted_items.values())
print(avg_value)

good_idx = set()
last_good_key = 0
temp_idx = dict()
for key, value in sorted_items.items():
    if value > avg_value - SCORE_BIAS:
        temp_idx[key] = value
        if key > last_good_key + FRAMES_GAP:
            good_idx.add(max(temp_idx.items(), key=lambda k: k[1])[0])
            temp_idx = dict()
        last_good_key = key
print(good_idx)

for key, value in sorted_items.items():
    if key not in good_idx:
        try:
            os.remove('frames/out-'+str(key)+'.jpg')
        except Exception:
            pass
