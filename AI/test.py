# -*- coding: utf-8 -*-
import cv2
import numpy as np

def is_cell_red(cell):
    return cell[3] > 180

def check_row(row):
    distance = 0
    large = 0
    

def detect(image):
    # BGR
    largest_distance = 0
    for row in np.array(image)[0]:
        print(row)
    
    

detect(cv2.imread('resources/test_img.PNG'))