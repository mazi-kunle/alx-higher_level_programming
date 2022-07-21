#!/usr/bin/python3
"""This is a module."""


class Square:
    """A Square class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """init function."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """A getter function for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """A setter function for position."""
        if ((not isinstance(value, tuple)) and len(value) != 2
                and value[0] < 0 and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """A method to print a square."""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                for j in range(self.__size):
                    print('#', end="")
                print()
