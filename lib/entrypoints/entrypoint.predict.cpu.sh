#!/bin/bash
set -e

BASE_MODEL_NAME=$1
WEIGHTS_FILE=$2
IMAGE_SOURCE=$3
VIDEO_SOURCE=$4
NO_CROP=$(echo $NO_CROP)
DRY_RUN=$(echo $DRY_RUN)

ACTION=$(echo $PREDICT_MODEL| cut -d'_' -f 3)
VIDEO_FILE=$(ls -1t /src/source|head -n 1)

if [ $ACTION == "technical" ]
then
    if [ $NO_CROP == "true" ]
    then
        ffmpeg -i /src/source/$VIDEO_FILE -qscale:v 2 "/src/frames/out-%01d.jpg"
    else
        ffmpeg -i /src/source/$VIDEO_FILE -filter:v "crop=1920:1023:0:0" -qscale:v 2 "/src/frames/out-%01d.jpg"
    fi
fi

# predict
python -m evaluater.predict \
--base-model-name $BASE_MODEL_NAME \
--weights-file $WEIGHTS_FILE \
--image-source $IMAGE_SOURCE

if [ $ACTION == "technical" ]
then
    if [ $DRY_RUN == "true" ]
    then
        python /src/entrypoints/run.py tech --dry-run
    else
        python /src/entrypoints/run.py tech
    fi
else
    if [ $DRY_RUN == "true" ]
    then
        python /src/entrypoints/run.py aes --dry-run
    else
        python /src/entrypoints/run.py aes
    fi
fi
