build:
	docker build -t highlights:latest .

run:
	docker build -t highlights:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app highlights:latest
