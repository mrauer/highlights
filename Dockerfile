FROM ubuntu:20.10

RUN apt-get update && apt-get install -y curl python

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python2.7 get-pip.py

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip==20.1.1 && \
    pip install -r requirements.txt
