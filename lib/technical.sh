#!/bin/bash

NO_CROP="false"
if [[ "$1" == *"no-crop"* ]]; then
  NO_CROP="true"
fi

DRY_RUN="false"
if [[ "$1" == *"dry-run"* ]]; then
  DRY_RUN="true"
fi

./lib/predict  \
    --docker-image highlights-cpu \
    --base-model-name MobileNet \
    --weights-file "$(pwd)"/lib/models/MobileNet/weights_mobilenet_technical_0.11.hdf5 \
    --image-source "$(pwd)"/frames \
    --video-source "$(pwd)"/source \
    --output-file "$(pwd)"/lib/output \
    --no-crop $NO_CROP \
    --dry-run $DRY_RUN
