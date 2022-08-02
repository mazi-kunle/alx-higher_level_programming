#!/usr/bin/python3
'''This is a module'''


class MyLsit(list):
    '''
    A My list class
    '''
    def print_sorted(self):
        '''
        print a list in ascending order.
        '''
        new_list = sorted(self)
        print(new_list)
