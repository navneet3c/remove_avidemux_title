#!/usr/bin/python3

## <navneetmails@gmail.com>

import argparse
import glob
import random
import string
import os
from subprocess import call

parser = argparse.ArgumentParser(prog="remove_avidemux_title", description='Removes "Avidemux" title from videos.')
parser.add_argument('-f', metavar="file_name", action="append", default="*.mkv",
    help="input file name. Supports wildcards. Can be specified multiple times. Default: %(default)s")
args = parser.parse_args()

files = glob.glob(args.f)
files.sort()
print("Processing files:", files)

tmp_file_prefix = "_remove_avidemux_nam_" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
for file in files:
    tmp_file = tmp_file_prefix + file
    call(["ffmpeg", "-i", file, "-map_metadata", "0", "-metadata", 'title=', "-codec", "copy", tmp_file])
    os.rename(tmp_file, file)

print("All Done.")
