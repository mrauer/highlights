.PHONY: frames

GLASSES_PATH=/Volumes/NO\ NAME/DCIM/Movie/*
SD_PATH=/Volumes/NO\ NAME/sd/*
OUTPUT_PATH=./output
SOURCE_PATH=./source

all: frames tech aes
assets: mp3 timelapse

help:
	@echo "  help          will display the help section."
	@echo "  all           will process a video."
	@echo "  vendor        will build the ML image."
	@echo "  clean         will remove the frames."

vendor:
	docker build -t nima-cpu lib/. -f lib/Dockerfile.cpu

clean:
	rm frames/*.jpg

frames:
	ffmpeg -i $(path) -ss $(start) -t 120 -qscale:v 2 "./frames/out-%01d.jpg"

tech:
	sh ./lib/technical.sh $(OPTS)

aes:
	sh ./lib/aesthetic.sh $(OPTS)

glasses:
	ls -ldh ${GLASSES_PATH} | awk '{print $$6, $$7, $$5, $$9"\\ "$$10}' 

sd:
	ls -ldh ${SD_PATH} | awk '{print $$6, $$7, $$5, $$9"\\ "$$10}' 

mp3:
	ffmpeg -i $(path) ${OUTPUT_PATH}/$(shell date +%FT%s).mp3

timelapse:
	ffmpeg -i $(path) -c:v libx265 -b:v 5000k -threads 4 -filter_complex "[0:v]setpts=1/6*PTS[v];[0:a]atempo=6[a]" -map "[v]" -map "[a]" ${OUTPUT_PATH}/$(shell date +%FT%s).mp4 && tput bel
