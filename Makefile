build:
	docker build -t highlights:latest .

run:
	docker build -t highlights:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app highlights:latest

vendor:
	docker build -t nima-cpu . -f lib/Dockerfile.cpu

frame:
	ffmpeg -i source/MOV00069.AVI -qscale:v 2 "frames/out-%01d.jpg"

tech:
	./lib/predict  \
    --docker-image nima-cpu \
    --base-model-name MobileNet \
    --weights-file $(pwd)/lib/models/MobileNet/weights_mobilenet_technical_0.11.hdf5 \
    --image-source $(pwd)/frames \
    --output-file $(pwd)/lib/output

quality:
	./lib/predict  \
    --docker-image nima-cpu \
    --base-model-name MobileNet \
    --weights-file $(pwd)/lib/models/MobileNet/weights_mobilenet_aesthetic_0.07.hdf5 \
    --image-source $(pwd)/frames \
    --output-file $(pwd)/lib/output
