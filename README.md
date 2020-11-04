# Highlights

Highlights is a software that detects the best moments of a video. You can transform a long video to a set of images retracing the best shots. Ideal for GoPro and any devices that records hours of videos.

<img src="./img/gallery.png" width="700px" />

## How does it work?

Multiple steps are necessary to extract the best moments from a video. The very first step is the conversion of the provided video to a set of images. This images will then go through two convolutional neural networks: one for technical aspects (blurry, on focus, etc...), and one for quality (ex: objects recognition). We keep a relatively high percentile of the best images from the initial set (85% for technical aspects, and 70% for aesthetic).

## How to use highlights?

You need to have <a href="https://www.docker.com/">Docker</a> installed. The rest will append within the container.

Add the video you want to process into the `/source` directory.

Then type the following set of commands:

```
make vendor (build the image)
make nocrop (process the video)
```

The output images will be available in the `/frames` directory at the end of the process.
