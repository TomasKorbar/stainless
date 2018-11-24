# -*- coding: utf-8 -*-
import requests
import cv2
import numpy as np
import PIL.Image as Image

def get_img():
    image_url = 'http://10.10.5.198:8080/photoaf.jpg'
    destination = 'resources/image'
    
    data = requests.get(image_url, stream=True, timeout=20)
    img = Image.open(data.raw)
    if image_url[-3:] == 'png':
        img.save(destination + '.png')
        img = cv2.imread(destination + '.png')
    else:
        img.save(destination + '.jpg')
        img = cv2.imread(destination + '.jpg')
    return img