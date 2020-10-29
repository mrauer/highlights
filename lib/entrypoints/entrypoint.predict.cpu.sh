#!/bin/bash
set -e

BASE_MODEL_NAME=$1
WEIGHTS_FILE=$2
IMAGE_SOURCE=$3
VIDEO_SOURCE=$4

ACTION=$(echo $PREDICT_MODEL| cut -d'_' -f 3)
VIDEO_FILE=$(ls -1t /src/source|head -n 1)

echo $PREDICT_MODEL
echo $ACTION

#if [[ $ACTION -eq "technical" ]]
if [ $ACTION == "technical" ]
then
  echo "HERE WE START FFMEG"
  ffmpeg -i /src/source/$VIDEO_FILE -qscale:v 2 "/src/frames/out-%01d.jpg"
fi

# predict
python -m evaluater.predict \
--base-model-name $BASE_MODEL_NAME \
--weights-file $WEIGHTS_FILE \
--image-source $IMAGE_SOURCE
