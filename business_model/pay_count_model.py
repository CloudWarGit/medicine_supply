'''
Created on 2017年12月23日

@author: CloudWar
'''

class PayModel(object):
    
    def __init__(self, name):
        self.name = name
        self.__pay_list = []
        self.__checkout_month = {}
            
    def put_pay_month(self, month, revenue=0):
        if revenue:
            self.__pay_list.append(dict(month=month, revenue=revenue))
            if len(self.__pay_list) >=3 :
                self.__checkout_month = self.__pay_list.pop(0)
        
    def get_payment(self, checkout_func=None):
        if checkout_func:
            self.__checkout_month=checkout_func(self.__checkout_monthß)
        return self.__checkout_month

    def _get_pay_list(self):
        return self.__pay_list
            
        