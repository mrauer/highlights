import json
import os
import re
import numpy as np

#SCORE_BIAS = -0.55
SCORE_BIAS = 0
FRAMES_GAP = 5

# Load from JSON file
f = open('./lib/output/technical.txt', 'r')
items = json.loads(f.read())

# Parsing and ordering.
sorted_items = dict()
for item in items:
    _id = int(re.findall(r'\d+', item['image_id'])[0])
    sorted_items[_id] = float(item['mean_score_prediction'])

for key, value in sorted_items.items():
    if float(value) <= np.percentile(sorted_items.values(), 85):
        try:
            #print 'removing' + str(key)
            os.remove('frames/out-'+str(key)+'.jpg')
        except Exception:
            pass
