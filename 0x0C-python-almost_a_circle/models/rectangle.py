#!/usr/bin/python3
'''This is a module'''


from base import Base


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
    def width(self):
        '''A setter function for width'''
        self.__width = width

    @property
    def height(self):
        '''A getter function for height'''
        return self.__height

    @height.setter
    def height(self):
        '''A setter function for height'''
        self.__height = height

    @property
    def x(self):
        '''A getter for x'''
        return self.__x

    @x.setter
    def x(self):
        '''A setter for x'''
        self.__x = x

    @property
    def y(self):
        '''A setter for y'''
        return self.__y

    @y.setter
    def y(self):
        '''A setter function for y'''
        self.__y = y
