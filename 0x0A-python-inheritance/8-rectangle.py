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


class Rectangle(BaseGeometry):
    '''
    This is a class that inherits from BaseGeometry class.
    '''
    def __init__(self, width, height):
        '''An init function'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
