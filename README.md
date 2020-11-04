# Highlights

Highlights is a software that detects the best moments of a video. You can transform a long video to a set of images retracing the best shots using simple AI. Ideal for GoPros or any devices that records hours of videos and for which you want to be able to get a gallery of the top quality images as well as storing it at a much lower space toll than with the original format.

<img src="./img/gallery.png" width="700px" />

## How does it work?

Multiple steps are necessary. The very first step is the conversion of the provided video to a set of images. These images will then go through two convolutional neural networks: one for technical aspects (blurry, on focus, etc...), and one for quality (ex: objects recognition). We keep a relatively high percentile of the best images from the initial set (85% for technical aspects, and 70% for aesthetic).

## How to use highlights?

You need to have <a href="https://www.docker.com/">Docker</a> installed. The rest will happend within the container.

Add the video you want to process into the `/source` directory (.avi extension).

Then type the following set of commands at the root of the project:

```
make vendor (build the docker image)
make nocrop (process the video end to end)
```

The output images will be available in the `/frames` directory at the end of the process.
