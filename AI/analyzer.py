# -*- coding: utf-8 -*-
"""
Code for automatic analyzation testing images
"""
from YOLO_small_tf import YOLO_TF
import os


def main():
    yolo = YOLO_TF()
    yolo.imshow = False
    yolo.filewrite_img = True
    
    dir_location = 'resources/neroztrideno/'
    files = os.listdir(dir_location)
    
    for file in files:
        yolo.tofile_img = 'resources/output/' + file
        yolo.detect_from_file(dir_location + file)


if __name__ == '__main__':
    main()
