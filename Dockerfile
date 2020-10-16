FROM ubuntu:20.10

#RUN apk add --no-cache python

#RUN apt-get update && apt-get install libsvm-dev python

WORKDIR /usr/src/app

COPY . .
