#!/usr/bin/env python3

from PIL import Image
import os
import sys
import subprocess # module to run processes in the command line

# If no directory path is specified, set the directory path
# to the current working directory
if len(sys.argv) == 1:
    # Get current working directory
    dir_path = os.getcwd()
else:
    # Get specified path
    dir_path = sys.argv[1]

    # Account for a possible trailing slash in the specified path
    if dir_path[-1] == "/":
        dir_path = dir_path[:-1]


#img_files = [img_file for img_file in os.listdir(dir_path) if os.path.splitext(img_file)[1] == ext]

img_files = []

for file in os.listdir(dir_path):

    # Get file extension
    ext = os.path.splitext(file)[1]

    # Filter out any non-image files
    if ext.lower() == '.jpg':
        img_files.append(file)


for i, filename in enumerate(img_files):
    
    num = f"{i+1:04}"

    filename_old = "{}/{}".format(dir_path, filename)
    filename_new = "{}/{}{}".format(dir_path, num, '.jpg')

    os.rename(filename_old, filename_new)

print("Renaming done!")