#!/bin/bash
set -e

BASE_MODEL_NAME=$1
WEIGHTS_FILE=$2
IMAGE_SOURCE=$3
VIDEO_SOURCE=$4
CROP_FLAG=$(echo $CROP_FLAG)

ACTION=$(echo $PREDICT_MODEL| cut -d'_' -f 3)
VIDEO_FILE=$(ls -1t /src/source|head -n 1)

if [ $ACTION == "technical" ]
then
    if [ $CROP_FLAG == "crop" ]
    then
        ffmpeg -i /src/source/$VIDEO_FILE -filter:v "crop=1920:1023:0:0" -qscale:v 2 "/src/frames/out-%01d.jpg"
    else
        ffmpeg -i /src/source/$VIDEO_FILE -qscale:v 2 "/src/frames/out-%01d.jpg"
    fi
fi

# predict
python -m evaluater.predict \
--base-model-name $BASE_MODEL_NAME \
--weights-file $WEIGHTS_FILE \
--image-source $IMAGE_SOURCE

if [ $ACTION == "technical" ]
then
  python /src/entrypoints/run.py tech
else
  python /src/entrypoints/run.py aes
fi
