#!/usr/bin/python

import os
import sys
import zipfile
import argparse
import string

parser = argparse.ArgumentParser(description='Zip textures for release')
parser.add_argument('-subset', dest='subset', help='The name of the subset of textures being packaged', required=True)
parser.add_argument('-version', dest='version', help='The version number of the pack', required=True)

args=parser.parse_args()

include_flist = args.subset + ".txt"
zip_name = "../releases/BlockStyle_v" + args.version + "_" + args.subset + ".zip"
if os.path.isfile(include_flist):
   with open(include_flist) as to_include:
      files = to_include.read().splitlines()   # files to include in archive
else:
   sys.exit("No input file for " + args.subset)

zfile = zipfile.ZipFile(zip_name, "w") # create zip file

for f in files: # add all files to zip
   if os.path.isfile(f):
      archive_name = f[len("../BlockStyle/"):]
      zfile.write(f, archive_name)
   else:
      sys.exit("No file in path " + f)

zfile.close()  # close zip
