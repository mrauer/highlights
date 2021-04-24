SD_PATH=/Volumes/NO\ NAME/DCIM/Movie/*
OUTPUT_PATH=./output
SOURCE_PATH=./source

all: tech aes

help:
	@echo "  help          will display the help section."
	@echo "  all           will process a video."
	@echo "  vendor        will build the ML image."
	@echo "  clean         will remove the frames."

vendor:
	docker build -t nima-cpu lib/. -f lib/Dockerfile.cpu

clean:
	rm frames/*.jpg

tech:
	sh ./lib/technical.sh $(OPTS)

aes:
	sh ./lib/aesthetic.sh $(OPTS)

sd:
	ls -ldh ${SD_PATH} | awk '{print $$6, $$7, $$5, $$9"\\ "$$10}' 

mp3:
	ffmpeg -i $(path) ${OUTPUT_PATH}/$(notdir $(path)).mp3

timelapse:
	ffmpeg -i $(path) -vcodec libx265 -crf 28 -filter_complex "[0:v]setpts=1/6*PTS[v];[0:a]atempo=6[a]" -map "[v]" -map "[a]" ${OUTPUT_PATH}/$(notdir $(path))

cut:
	ffmpeg -i $(path) -ss $(start) -t $(end) ${SOURCE_PATH}/$(notdir $(path))
