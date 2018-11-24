# -*- coding: utf-8 -*-
import logging
from YOLO_small_tf import YOLO_TF
from api_caller import APICaller
from image_func import get_img
import move_enum 

logging.basicConfig(filename='app.log', level=logging.DEBUG)

api = APICaller()
yolo = YOLO_TF()

yolo.imshow = False

bottle_class = 'bottle'
degres = 120


def calculate_percentage(x_start, x_stop, img_w):
    middle = ((x_stop - x_start) / 2) + x_start
    logging.debug('Percentage: ' + str(middle / img_w))
    return middle / img_w
    
def calculate_left_deg(percentage):
    degres_half = degres / 2
    percentage_calculation = 1.0 - (percentage * 2)
    logging.debug('calculate_left_deg: ' + str(degres_half * percentage_calculation))
    
    return degres_half * percentage_calculation

def calculate_right_deg(percentage):
    degres_half = degres / 2
    percentage = percentage - 0.50
    logging.debug('calculate_right_deg: ' + str(degres_half * (percentage * 2)))
    
    return degres_half * (percentage * 2)
    

def process_bottle(data):
    """
    param:
        data: [1619.5781, 2630.89, 1888.886, 2985.486]
              [X start,   X stop,  Y - start, Y - stop]
            output of yolo detector without class and percentage
    """
    
    img_w = yolo.w_img
    img_h = yolo.h_img
    
    logging.debug('result (process_bottle): ')
    logging.debug(data)
    percentage = calculate_percentage(data[0], data[1], img_w)
    print('Percentage: ' + str(percentage))
    
    deviation = 0.07
    
    if 0.50 + deviation >= percentage >= 0.50 - deviation:
        print('Forward pass')
        return api.move_forward(30)
    elif percentage > 0.50:
        print('Right rotate: ' + str(calculate_right_deg(percentage)))
        api.turn_right(calculate_right_deg(percentage))
        return False
    else:
        print('Left rotate: ' + str(calculate_left_deg(percentage)))
        api.turn_left(calculate_left_deg(percentage))
        return False
    
    return False

def filter_results(results):
    result = []
    for res in results:
        if res[0] == bottle_class:
            result.append(res)
    
    return result

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

def navigate_to_bottle(result):
    logging.debug('inside navigate_to_bottle func')
    logging.debug('result of detection: ')
    logging.debug(result)
    process_result = process_bottle(result[0][1:-1])
    
    while True:
        img = get_img()
        yolo.detect_from_cvmat(img)
        vision_result = filter_results(yolo.result)
        logging.debug('result of detection: ')
        logging.debug(vision_result)
        if len(vision_result) == 0: # no catch
            result = api.move_forward(20)
            if result:
                api.pick_up()
                break
        else:
            logging.debug('I can see a bottle')
            result = process_bottle(vision_result[0][1:-1])
            if result:
                api.pick_up()
                break


def ultimate_finding_cycle():
    
    while True:
        img = get_img()
        yolo.detect_from_cvmat(img)
        result = filter_results(yolo.result)
        if len(result) == 1:
            navigate_to_bottle(result)
            break
        else:
            logging.debug('ultimate_finding_cycle can´t see anythink')
            api.turn_right(10)
            #api.move_forward(1)
        
        
        


def main():
    ultimate_finding_cycle()

if __name__ == '__main__':    
    main()
