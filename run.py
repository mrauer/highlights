import json
import os
import re
import sys

import numpy as np

FRAMES_GAP = 30
TECHNICAL_PATH = './lib/output/technical.txt'
AESTHETIC_PATH = './lib/output/aesthetic.txt'
TECHNICAL_PERCENTILE = 85
AESTHETIC_PERCENTILE = 70


def process_tech():
    # Load from JSON file
    f = open(TECHNICAL_PATH, 'r')
    items = json.loads(f.read())

    # Parsing and ordering.
    sorted_items = dict()
    for item in items:
        _id = int(re.findall(r'\d+', item['image_id'])[0])
        sorted_items[_id] = float(item['mean_score_prediction'])

    for key, value in sorted_items.items():
        if float(value) <= np.percentile(
             sorted_items.values(), TECHNICAL_PERCENTILE):
            try:
                os.remove('frames/out-'+str(key)+'.jpg')
            except Exception:
                pass


def process_aes():
    # Load from JSON file
    f = open(AESTHETIC_PATH, 'r')
    items = json.loads(f.read())

    # Parsing and ordering.
    sorted_items = dict()
    for item in items:
        _id = int(re.findall(r'\d+', item['image_id'])[0])
        sorted_items[_id] = float(item['mean_score_prediction'])

    good_idx = set()
    last_good_key = 0
    temp_idx = dict()
    for key, value in sorted_items.items():
        if value > np.percentile(sorted_items.values(), AESTHETIC_PERCENTILE):
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


if sys.argv[1] == 'aes':
    process_aes()

if sys.argv[1] == 'tech':
    process_tech()
