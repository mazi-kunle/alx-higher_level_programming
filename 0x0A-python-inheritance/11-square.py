#!/usr/bin/python3
'''This is a module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    This is a Square class that inherits from the Rectangle class.
    '''
    def __init__(self, size):
        '''An init function'''
        self.__size = size
        super().__init__(size, size)
