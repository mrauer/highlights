import json
import os
import re
import numpy as np

#SCORE_BIAS = -0.55
SCORE_BIAS = 0
FRAMES_GAP = 5

# Load from JSON file
f = open('tech.json', 'r')
items = json.loads(f.read())

# Parsing and ordering.
sorted_items = dict()
for item in items:
    _id = int(re.findall(r'\d+', item['image_id'])[0])
    sorted_items[_id] = float(item['mean_score_prediction'])

#print sorted_items
#res = {k: np.percentile(v, 75) for k, v in sorted_items.items()}

#print res
#print len(res)
#print np.percentile(sorted_items.values(), 75)

#max_value = max(sorted_items.items(), key=lambda k: k[1])[1]
for key, value in sorted_items.items():
#    print 'a'+str(value)
#    print max_value* 0.75
    if float(value) <= np.percentile(sorted_items.values(), 85):
        print 'ok'
        try:
            #print 'removing' + str(key)
            os.remove('frames/out-'+str(key)+'.jpg')
        except Exception:
            pass

        #print value

#print sorted(sorted_items.items(), key=lambda k: k[1])