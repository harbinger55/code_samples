#!/usr/bin/python

import os
import shutil

baseDirectory = "./moveit" # The directory to work on

# See if the directory exists, if not create it.  Kind of pointless since there or no files to move then, but it supresses an error
try:
    os.stat(baseDirectory)
except:
    os.mkdir(baseDirectory) 

for filez in os.listdir(baseDirectory): # read the directory one file at a time
  if not filez.endswith(".htm"): # if the file does not end with .htm skip it
    next
  else:
    shortName = os.path.splitext(filez)[0] #get the file name stripped of the extention
    shutil.move(baseDirectory + "/" + shortName + ".htm", baseDirectory + "/" + shortName + ".html") # move the file from .htm to .html

