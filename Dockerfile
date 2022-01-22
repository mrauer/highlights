FROM tensorflow/tensorflow:2.7.0

RUN apt update && apt install -y python3-pip=20.0.2-5ubuntu1.6 && \
    pip3 install Pillow==9.0.0

WORKDIR /src

COPY lib/src .
