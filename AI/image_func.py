# -*- coding: utf-8 -*-
import requests
import cv2
import numpy as np
import PIL.Image as Image

def get_img():
    image_url = 'http://localhost/img_test.jpg'
    destination = 'resources/image'
    
    data = requests.get(image_url, stream=True, timeout=8)
    img = Image.open(data.raw)
    if image_url[-3:] == 'png':
        img.save(destination + '.png')
        img = cv2.imread(destination + '.png')
    else:
        img.save(destination + '.jpg')
        img = cv2.imread(destination + '.jpg')
    
    return img