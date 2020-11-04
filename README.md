# Highlights

Highlights is a software that detects the best moments of a video. You can transform a long video to a set of images retracing the best shots.

<IMG>

## How does it work?

Multiple steps are necessary to extract the best moments from a video. The very first step is the conversion of the provided video to a set of images. This images will then go through two `Convolutional neural network`: one for technical aspects (blurry, on focus, etc...), and one for quality (ex: objects recognition). We keep a relatively high percentile of the best images from the initial set.

## How to use highlights?

You need to have Docker installed. The rest will append within the container.

Add the video you want to process into the `/source` directory.

Then type the following set of commands:

```
make vendor (build the image)
make nocrop (process the video)
```

The output images will be available in the `/frames` directory at the end of the process.
