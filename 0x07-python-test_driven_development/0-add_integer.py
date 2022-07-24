#!/usr/bin/python3
'''This is a module that contains an add_integer function'''


def add_integer(a, b=98):
    '''
    a and b must be integers or floats, otherwise raise a
    TypeError exception with the message a must be an integer
    or b must be an integer

    a and b must be first casted to integers if they are float.

    Returns an integer: the addition of a and b.
    '''
    if (type(a) != int and type(a) != float):
        raise TypeError('a must be an integer')
    elif (type(b) != int and type(b) != float):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
