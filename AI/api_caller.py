# -*- coding: utf-8 -*-
import requests
import logging

class APICaller():
    url = 'http://10.10.4.66:5000'
    timeout = 120
    
    def __init__(self):
        self.logger = logging.getLogger('APICaller')
    
    def turn_left(self, angle):
        """
        Calls robot´s API to turn him left
        param:
            angle: number of degrees whitch robot will be turned to left
        
        returns:
            True after robot ends the operation or False if somethink failed
        raise:
            ValueError if angle is negative
        """
        if angle > 0:
            logging.critical('Angle is negative ' + str(angle))
        
        return self.__send_turn_request(angle=angle * (-1))
    
    def turn_right(self, angle):
        logging.debug('Turning right')
        return self.__send_turn_request(angle=angle)
    
    def move_forward(self, cm):
        
        params = {'cm': 1}
        i = 0
        
        while i < cm:
            
            try:
                self.logger.debug('Sending move_forward request ({0} cm)'.format(cm))
                response = requests.get(self.url + '/move/forward', params=params, timeout=self.timeout)
                is_in_range_response = requests.get(self.url + '/trash/isinrange', timeout=self.timeout)
            except requests.exceptions.Timeout:
                self.logger.warn('move_forward timeout exception')
                #return False
        
            if not response.ok or not is_in_range_response.ok:
                self.logger.error('Response is not OK')
                #return False
        
            #self.logger.debug('Response: ' + str(response.json()))
            if is_in_range_response.json() == True:
                return True
            
            
        return False
    
    def is_in_range(self):
        """
        return: True of False
        raise: TimeoutException
        """
        self.logger.debug('Sending is_in_range request')
        response = requests.get(self.url + '/trash/isinrange', timeout=self.timeout)
        self.logger.debug('Response: ' + str(response.json()))
        
        return response.json()
    
    def pick_up(self):
        """
        return: True if is everithing OK
        raise: TimeoutException
        """
        self.logger.debug('Sending pick_up request')
        response = requests.get('trash/pickup', timeout=self.timeout)
        if not response.ok:
            self.logger.error('Response is not OK')
            return False
        
        self.logger.debug('Response: ' + str(response.json()))
        return response.json()
        
    
    def __send_turn_request(self, angle):

        params = {'angle': angle}
        try:
            self.logger.debug('Sending turn request ({0} angle)'.format(angle))
            response = requests.get(self.url + '/move/turn', params=params, timeout=self.timeout)
        except requests.exceptions.Timeout:
            self.logger.warn('turn request timeout exception')
            return False
        
        if not response.ok:
            self.logger.error('Response is not OK')
            return False
        
        self.logger.debug('Response: ' + str(response.json()))
        return response.json()
    
    
    
        
        
        
        
        
    