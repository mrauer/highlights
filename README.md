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

## Bulk Processing

It is now possible to bulk process a list of videos.

This is the command:

```sh
python3 bulk.py --jobs <num_videos_to_process>
```

Before using this feature, you must see the following environment variables:

```sh
HIGHTLIGHTS_SOURCE_PATH (where you list of *.mp4 is located)
HIGHTLIGHTS_OUTPUT_PATH (where to store the final pictures + timelapse)
```

## Additional commands

```sh
make sd (get list of videos on SD card)
make glasses (get list of videos on Glasses)
make assets path="<video_path>" (creates mp3 + timelapse)
make all path="<video_path>" start=<start_second> (process from start seconds, 2 min chunk)
```

## Credits

Credits to https://github.com/idealo/image-quality-assessment under Apache-2.0 License for which the code is partially used in this project.
