# Highlights

Highlights is a software that detects the best moments of a video. You can transform a long video to a set of images retracing the best shots using simple AI. Ideal for GoPros or any devices that records hours of videos and for which you want to be able to get a gallery of the top quality images as well as storing it at a much lower space toll than with the original format.

<img src="./img/gallery.png" width="700px" />

## How does it work?

Multiple steps are necessary. The very first step is the conversion of the provided video to a set of images. These images will then go through two convolutional neural networks: one for technical aspects (blurry, on focus, etc...), and one for quality (ex: objects recognition). We keep just of small amount of images from the initial set (above 85% percentile for technical aspects, and 70% percentile for aesthetic).

## How to use highlights?

You need to have <a href="https://www.docker.com/">Docker</a> installed. The rest will happen within the container.

Add the video you want to process into the `/source` directory (.avi extension).

Then type the following set of commands at the root of the project:

```sh
make all (process all)
make all OPTS="no-crop" (don't crop the video, keep timestamp)
make all OPTS="dry-run" (do not delete frames)
make all OPTS="dry-run,no-crop" (both options)
make clean (remove all frames)
```

The output images will be available in the `/frames` directory at the end of the process.

## Additional commands

```sh
make sd (get list of videos on SD card)
make mp3 path="<video_path>" (extract the sound of a video as mp3)
make timelapse path="<video_path>" (make a timelapse from the video)
make cut path="/Volumes/NO\ NAME/DCIM/Movie/2001_0204_192734_058.MP4" start=0 end=60 (cut a video)
```

## Credits

Credits to https://github.com/idealo/image-quality-assessment under Apache-2.0 License for which the code is partially used in this project.
