import argparse
import glob
import os
import sys
import time

HIGHTLIGHTS_SOURCE_PATH = os.environ['HIGHTLIGHTS_SOURCE_PATH']
HIGHTLIGHTS_OUTPUT_PATH = os.environ['HIGHTLIGHTS_OUTPUT_PATH']
RATIO = 15  # ratio space needed vs. disk.
DEFAULT_NUM_JOBS = 1
ERROR_CODE = 1


def available_space_bytes():
    disk = os.statvfs('/')
    return (disk.f_bavail * disk.f_frsize)


def get_next_file():
    files = filter(os.path.isfile, glob.glob(HIGHTLIGHTS_SOURCE_PATH + '*'))
    files = sorted(files, key=lambda x: os.stat(x).st_size)
    for file in files:
        if os.stat(file).st_size * RATIO < available_space_bytes():
            return file.replace(' ', '\\ ')
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
