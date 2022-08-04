#!/usr/bin/python3
'''This is a module'''


class Student:
    '''A student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        A function that returns an instance attribute.
        '''
        return self.__dict__
