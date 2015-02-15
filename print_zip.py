__author__ = 'sam'

import argparse

from zipfile import ZipFile

def label(bytes):
    suffixes = [" bytes", "KB","MB", "GB"]
    i = 0
    divisor = 1.0
    while bytes > divisor*1000:
        divisor *= 1000
        i += 1
    return str(round(bytes * 10 / divisor) * 0.1) + suffixes[i]

def get_data(zip_file):
    return [(info.filename, label(info.file_size))for info in zip_file.infolist()]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    input_file = args.input_file

    zipped = ZipFile(input_file)
    listings = get_data(zipped)
    for file_info in listings:
        print "%-70s %s" % (file_info[0], file_info[1])

