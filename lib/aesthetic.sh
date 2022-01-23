#!/bin/bash

./lib/predict  \
    --docker-image highlights-cpu \
    --base-model-name MobileNet \
    --weights-file "$(pwd)"/lib/models/MobileNet/weights_mobilenet_aesthetic_0.07.hdf5 \
    --image-source "$(pwd)"/frames \
    --video-source "$(pwd)"/source \
    --output-file "$(pwd)"/lib/output \
