#!/usr/bin/python3
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
