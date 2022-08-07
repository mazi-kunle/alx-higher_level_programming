#!/usr/bin/python3
'''This is a module'''


from models.base import Base


class Rectangle(Base):
    '''A class that inherits from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''A getter function for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''A setter function for width'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''A getter function for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''A setter function for height'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''A getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''A setter for x'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''A setter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''A setter function for y'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
