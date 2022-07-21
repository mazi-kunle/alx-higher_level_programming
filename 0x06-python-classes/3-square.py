#!/usr/bin/python3
"""This is a module"""


class Square:
    """A Square class that defines a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A method to get the area of a sqaure"""
        return (self.__size ** 2)
