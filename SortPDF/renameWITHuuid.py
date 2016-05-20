#!/usr/bin/python

import os
import shutil
import sys
import argparse
import uuid
import fnmatch

parser = argparse.ArgumentParser()

parser.add_argument("--dir", help="Source Path")

args = parser.parse_args()

tilefiles = []

for root, dirs, files in os.walk(args.dir):
     for name in fnmatch.filter(files, "*title*"):
        tilefiles.append(os.path.join(root, name))

if len(tilefiles) == 0:
    sys.stdout("Error no title file!")

for titlefile_path in tilefiles:

    unsortedfile = os.path.join(os.path.dirname(titlefile_path),str(uuid.uuid1())+".pdf")
  
    try:
        shutil.move(titlefile_path, unsortedfile)
    except:
        print("can not move file %s -> %s" % (titlefile_path, unsortedfile))