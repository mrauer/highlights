all: tech aes
temp: crop aes

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
	sh ./lib/technical.sh nocrop

crop:
	sh ./lib/technical.sh crop

aes:
	sh ./lib/aesthetic.sh
