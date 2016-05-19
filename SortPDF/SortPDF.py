#!/usr/bin/python

import os
import shutil
import argparse
import fnmatch
from PyPDF2 import PdfFileWriter, PdfFileReader

parser = argparse.ArgumentParser()

parser.add_argument("--verbosity", default=0, help="increase output verbosity", type=int)
parser.add_argument("--destination", help="Destination Path")
parser.add_argument("--source", help="Source Path")

args = parser.parse_args()

dest = args.destination
src = args.source
vlevel = args.verbosity

if not os.path.exists(src):
    sys.stderr("source path does not exists!!!")

if not os.path.exists(dest):
    os.mkdir(dest)
    if vlevel > 1:
            print("create destination")

pdffiles = []

i=0

for root, dirs, files in os.walk(src):

    for name in fnmatch.filter(files, "*.pdf"):
        pdffiles.append(os.path.join(root, name))

        if vlevel > 1:
            print(os.path.join(root, name))

if len(pdffiles) == 0:
    sys.stdout("Error no pdf file!")

for pdffile_path in pdffiles:

    if vlevel > 1:
        print('try opening pdf file %s' % pdffile_path)
    try:
        pdffile = PdfFileReader(pdffile_path, "rb")
 

        if vlevel > 2:
            print('Title %s.' % pdffile.getDocumentInfo().title)
            print('Author %s' % pdffile.getDocumentInfo().author)
            print('Subject %s' % pdffile.getDocumentInfo().subject)
            print('Creator %s' % pdffile.getDocumentInfo().creator)
            print('producer %s' % pdffile.getDocumentInfo().producer)

        title = pdffile.getDocumentInfo().title
        author = pdffile.getDocumentInfo().author
        subject = pdffile.getDocumentInfo().subject
    
    except:
        print('pdf file error %s' % pdffile_path)
        continue
        
    if not title:
        title = "no_title" + str(i)
        i = i + 1

    if not author:
        author = "various"

    if not subject:
        subject = "no_subject"

    subjectpath = os.path.join(dest, subject)
    authorpath = os.path.join(subjectpath, author)
    try:
        if not os.path.exists(subjectpath):
            os.mkdir(subjectpath)
            os.mkdir(authorpath)
            if vlevel > 1:
                print(subjectpath)
                print(authorpath)
        
        if not os.path.exists(authorpath):
            os.mkdir(authorpath)
            if vlevel > 1:
                print(authorpath)
            
        shutil.move(pdffile_path, authorpath+"/"+os.path.basename(title)+".pdf")

        if vlevel > 0:
            print("PDF File is %s" % pdffile)
            print("Copy to %s" % authorpath+"/"+os.path.basename(pdffile_path))

    except:
        print("cannot move file %s" % authorpath+"/"+os.path.basename(pdffile_path))
        continue