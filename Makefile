all: tech aes

help:
	@echo "  help          displays the help section."
	@echo "  vendor        build the ML image."
	@echo "  frame         arg video=MOV00069.AVI converts video to frames."
	@echo "  all           identify best images in set of frames."

build:
	docker build -t highlights:latest .

run:
	docker build -t highlights:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app highlights:latest

vendor:
	docker build -t nima-cpu lib/. -f lib/Dockerfile.cpu

clean:
	rm frames/*.jpg

frame:
	ffmpeg -i source/$(video) -qscale:v 2 "frames/out-%01d.jpg"

tech:
	sh ./lib/technical.sh && make exec action=tech

aes:
	sh ./lib/aesthetic.sh && make exec action=aes

exec:
	python ./run.py $(action)
