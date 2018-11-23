# -*- coding: utf-8 -*-
from YOLO_small_tf import YOLO_TF
import time

yolo = YOLO_TF()

yolo.imshow = False
s = time.time()
yolo.detect_from_file('resources/test.jpg')
print('Detection time: ' + str(time.time()-s))
    
result = yolo.result

print('result')