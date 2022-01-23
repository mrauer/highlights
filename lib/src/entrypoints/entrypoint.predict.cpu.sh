#!/bin/bash
set -e

BASE_MODEL_NAME="$1"
WEIGHTS_FILE="$2"
IMAGE_SOURCE="$3"

ACTION="$(echo "$PREDICT_MODEL"| cut -d'_' -f 3)"

# predict
python3 -m evaluater.predict \
--base-model-name "$BASE_MODEL_NAME" \
--weights-file "$WEIGHTS_FILE" \
--image-source "$IMAGE_SOURCE"

if [ "$ACTION" == "technical" ]
then
    python3 /src/entrypoints/run.py tech
else
    python3 /src/entrypoints/run.py aes
fi
