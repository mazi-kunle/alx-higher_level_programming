#!/usr/bin/python3
'''This is a module'''


class BaseGeometry:
    '''This is a class'''
    def area(self):
        '''An area class'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        A method that validates that value in an integer.
        '''
        if (type(value) != int):
            raise TypeError(f'{name} must be an integer')
        elif (value <= 0):
            raise ValueError(f'{name} must be greater than 0')
