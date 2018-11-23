# -*- coding: utf-8 -*-
import logging
from YOLO_small_tf import YOLO_TF
from motor_functions import turn_left, turn_right, forward

logging.basicConfig(file='app.log', level=logging.DEBUG)

yolo = YOLO_TF()

yolo.imshow = False

bottle_class = 'bottle'
degres = 120


def calculate_percentage(x_start, x_stop, img_w):
    middle = ((x_stop - x_start) / 2) + x_start
    return middle / img_w
    
def calculate_left_deg(percentage):
    degres_half = degres / 2
    percentage_calculation = 0.100 - (percentage * 2)
    
    return degres_half * percentage_calculation

def calculate_right_deg(percentage):
    degres_half = degres / 2
    percentage = percentage - 0.50
    
    return degres_half * (percentage * 2)
    

def detect(filename):
    import time
    s = time.time()
    yolo.detect_from_file(filename)
    print('Detection time: ' + str(time.time()-s))
    
    result = filter_results(yolo.result)
    
    print('result')
    print(result)
    
    """
    RESULT:
    [['bottle', 1619.5781, 2630.89, 1888.886, 2985.486, 0.7833293080329895]]
    """
    
    if len(result) > 1:
        print('Multiple results !!!')
        return;

    
    if len(result) == 0:
        print('Oh f*ck ... there is no bottle')
        return;
    
    process_bottle(result[0][1:-1])
    


def main():
    detect('flasky/4.jpg')


main()
