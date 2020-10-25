./lib/predict  \
    --docker-image nima-cpu \
    --base-model-name MobileNet \
    --weights-file $(pwd)/lib/models/MobileNet/weights_mobilenet_aesthetic_0.07.hdf5 \
    --image-source $(pwd)/frames \
    --output-file $(pwd)/lib/output
