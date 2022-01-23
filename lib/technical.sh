#!/bin/bash

./lib/predict  \
    --docker-image highlights-cpu \
    --base-model-name MobileNet \
    --weights-file "$(pwd)"/lib/models/MobileNet/weights_mobilenet_technical_0.11.hdf5 \
    --image-source "$(pwd)"/frames \
    --video-source "$(pwd)"/source \
    --output-file "$(pwd)"/lib/output
