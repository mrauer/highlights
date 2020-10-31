import base64
import hashlib
import json
import os
import re
import sys
import time
from collections import OrderedDict

import numpy as np

FRAMES_GAP = 30
TECHNICAL_PATH = '../src/output/technical.txt'
AESTHETIC_PATH = '../src/output/aesthetic.txt'
TECHNICAL_PERCENTILE = 85
AESTHETIC_PERCENTILE = 70
FRAMES_DIR = '../src/frames/'


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
             list(sorted_items.values()), TECHNICAL_PERCENTILE):
            try:
                os.remove('../src/frames/out-'+str(key)+'.jpg')
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

    good_idx = list()
    last_good_key = 0
    temp_idx = dict()
    aes_limit = np.percentile(
        list(sorted_items.values()), AESTHETIC_PERCENTILE)
    sorted_dict = OrderedDict(sorted(sorted_items.items(), key=lambda t: t[0]))

    max_value = 0
    for key, value in sorted_dict.items():
        if value > aes_limit:
            if key > max_value + FRAMES_GAP:
                temp_idx[key] = value
            if key > last_good_key + FRAMES_GAP:
                max_value = max(temp_idx, key=temp_idx.get)
                good_idx.append(max_value)
                temp_idx = dict()
            last_good_key = key
    print(good_idx)

    for key, value in sorted_items.items():
        if key not in good_idx:
            try:
                os.remove('../src/frames/out-'+str(key)+'.jpg')
            except Exception:
                pass


def generate_hash():
    h = hashlib.sha1(str(time.time()).encode('utf-8')).digest()
    return re.sub(
        r'[^A-Za-z0-9 ]+', '',
        base64.b64encode(h).decode('utf-8')[:8])


def bulk_rename():
    files = os.listdir(FRAMES_DIR)
    _hash = generate_hash()
    for index, file in enumerate(files):
        os.rename(os.path.join(FRAMES_DIR, file), os.path.join(
            FRAMES_DIR, file.replace('out', _hash)))
        print(file)


if sys.argv[1] == 'tech':
    process_tech()

if sys.argv[1] == 'aes':
    process_aes()
    bulk_rename()
