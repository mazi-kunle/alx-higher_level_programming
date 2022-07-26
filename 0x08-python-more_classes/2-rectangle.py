#!/usr/bin/python3
'''This is a module'''


class Rectangle:
    '''An empty rectangle class'''
    def __init__(self, width=0, height=0):
        '''An init function'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''A getter function'''
        return self.__width

    @width.setter
    def width(self, value):
        '''A setter function'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''A getter function'''
        return self.__height

    @height.setter
    def height(self, value):
        '''A setter function'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Returns the area of a rectangle.'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns the perimeter'''
        return 2 * (self.__width + self.__height)
