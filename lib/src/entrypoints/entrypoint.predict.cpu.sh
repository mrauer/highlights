#!/bin/bash
set -e

BASE_MODEL_NAME=$1
WEIGHTS_FILE=$2
IMAGE_SOURCE=$3
VIDEO_SOURCE=$4
DRY_RUN=$(echo $DRY_RUN)

ACTION=$(echo $PREDICT_MODEL| cut -d'_' -f 3)

# predict
python3 -m evaluater.predict \
--base-model-name $BASE_MODEL_NAME \
--weights-file $WEIGHTS_FILE \
--image-source $IMAGE_SOURCE

if [ $ACTION == "technical" ]
then
    if [ $DRY_RUN == "true" ]
    then
        python3 /src/entrypoints/run.py tech --dry-run
    else
        python3 /src/entrypoints/run.py tech
    fi
else
    if [ $DRY_RUN == "true" ]
    then
        python3 /src/entrypoints/run.py aes --dry-run
    else
        python3 /src/entrypoints/run.py aes
    fi
fi
