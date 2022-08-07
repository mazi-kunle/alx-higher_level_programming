#!/usr/bin/python3
'''This is a module'''


from models.base import Base


class Square(Rectangle):
    '''A class that inherits from Rectangle class.'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format(
            id, x, y, width))
