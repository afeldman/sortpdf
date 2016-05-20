#!/usr/bin/python
import os, time, shutil, sys, argparse

parser = argparse.ArgumentParser()

parser.add_argument("--dir", help="Source Path")

args = parser.parse_args()

for dirpath, dirnames, files in os.walk(args.dir, topdown = False):
    if not os.listdir(dirpath)==[]:
        continue
    else:
        os.rmdir(dirpath)