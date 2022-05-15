from glob import glob

import cv2

import os
import numpy as np

import re

digits = re.compile(r'(\d+)')
_nsre = re.compile('([0-9]+)')


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]


def tokenize(filename):
    return tuple(int(token) if match else token
                 for token, match in
                 ((fragment, digits.search(fragment))
                  for fragment in digits.split(filename)))


## put full_path here and put a name for your mp4 video, e.g.: /Users/jim/Desktop/video.mp4
video_name = '/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/video.mp4'
#C:/Users/wsesr/Desktop/Lectures/COMP1804-AML/MLproject
## the images of the provided dataset should be extracted to a folder; privide here the full path to that folder and then add: /*')
## e.g.: /Users/jim/Desktop/dataset/*
#C:/Users/wsesr/Desktop/Lectures/COMP1804-AML/Project/vol/deform/dk15/attribute_db/emotionet_6/all
images = glob('/Users/wsesr/Desktop/Lectures/COMP1804-AML/Project/vol/deform/dk15/attribute_db/emotionet_6/all/*')
images.sort(key=natural_sort_key)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

video = cv2.VideoWriter(video_name, fourcc, 1, (1280, 720))

#out = cv2.VideoWriter('Videos/output.mp4',fourcc, fps, (1080,1080))

for image in images:
    video.write(cv2.resize(cv2.imread(image), (1280, 720)))


video.release()

## put full_path here and put a name for your text file that will list the name of the images in the order they are merged to form the video, e.g.: /Users/jim/Desktop/image_names.txt
#C:/Users/wsesr/Desktop/Lectures/COMP1804-AML/MLproject
file_name = '/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/image_names.txt'
with open(file_name, 'w') as fil:
    for image in images:
        fil.write(image + '\n')