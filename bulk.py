import argparse
import glob
import os
import subprocess
import sys
import time

HIGHTLIGHTS_SOURCE_PATH = os.environ['HIGHTLIGHTS_SOURCE_PATH']
HIGHTLIGHTS_OUTPUT_PATH = os.environ['HIGHTLIGHTS_OUTPUT_PATH']
RATIO = 15  # ratio space needed vs. disk.
DEFAULT_NUM_JOBS = 1
ERROR_CODE = 1
FFPROBE_CMD = 'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{}"'
FFMPEG_CMD = 'ffmpeg -i "{}" -ss {} -t {} "{}"'
RM_CMD = 'rm "{}"'


def available_space_bytes():
    disk = os.statvfs('/')
    return (disk.f_bavail * disk.f_frsize)


def cut_file_in_half(file_path):
    ret = 1
    duration_cmd = subprocess.check_output(FFPROBE_CMD.format(file_path), shell=True)
    duration = int(float(duration_cmd.decode("utf-8") .replace('\n', '')))
    half_duration = int(duration / 2)
    # first chunk.
    first = os.system(FFMPEG_CMD.format(file_path, '0', str(half_duration), ''.join([file_path.split('.')[0], '_first.mp4'])))
    # second chunk.
    second = os.system(FFMPEG_CMD.format(file_path, str(half_duration), str(half_duration), ''.join([file_path.split('.')[0], '_second.mp4'])))
    if first + second == 0:
        ret = os.system(RM_CMD.format(file_path))
    return ret


def get_next_file():
    files = filter(os.path.isfile, glob.glob(HIGHTLIGHTS_SOURCE_PATH + '*'))
    files = sorted(files, key=lambda x: os.stat(x).st_size)
    for file in files:
        if os.stat(file).st_size * RATIO < available_space_bytes():
            return file.replace(' ', '\\ ')
        # file is too large, divide in 2.
        ret = cut_file_in_half(file)
        if ret == ERROR_CODE:
            break
    return ERROR_CODE


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--jobs')
    parsed_args = p.parse_args()

    num_jobs = int(parsed_args.jobs) if parsed_args.jobs else DEFAULT_NUM_JOBS

    i = 0
    while i < num_jobs:
        next_file_path = get_next_file()
        if next_file_path == 1:
            return ERROR_CODE

        destination_path = '{}/{}'.format(HIGHTLIGHTS_OUTPUT_PATH, str(time.time())[:10])

        print('Processing {} with destination {}'.format(next_file_path, destination_path))

        os.system('make all path="{}" start=0 && mkdir {} && mv frames/*.jpg {} && make assets path="{}" && mv output/*.mp* {} && rm {}'.format(next_file_path, destination_path, destination_path, next_file_path, destination_path, next_file_path))
        i += 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
