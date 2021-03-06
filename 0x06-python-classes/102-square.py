#!/usr/bin/python3
"""This is a module."""


class Square:
    """A Square class that defines a square"""
    def __init__(self, size=0):
        """init function."""
        self.size = size

    def area(self):
        """A method to get the area of a sqaure"""
        return (self.__size ** 2)

    @property
    def size(self):
        """A getter function."""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter function."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        '''A magic method for equality'''
        return self.area() == other.area()

    def __ge__(self, other):
        '''A magic method for >='''
        return self.area() >= other.area()

    def __gt__(self, other):
        '''A magic method for >'''
        return self.area() > other.area()

    def __ne__(self, other):
        '''A magic method for !='''
        return self.area() != other.area()

    def __le__(self, other):
        '''A magic method for <='''
        return self.area() <= other.area()

    def __lt__(self, other):
        '''A magic method for <'''
        return self.area() < other.area()
