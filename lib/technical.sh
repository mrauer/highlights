./lib/predict  \
    --docker-image nima-cpu \
    --base-model-name MobileNet \
    --weights-file $(pwd)/lib/models/MobileNet/weights_mobilenet_technical_0.11.hdf5 \
    --image-source $(pwd)/frames \
    --output-file $(pwd)/lib/output
