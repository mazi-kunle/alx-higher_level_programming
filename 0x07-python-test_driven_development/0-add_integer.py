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
    if (type(a) != int or type(b) != int or
            type(a) != float or type(b) != float):
        raise TypeError('a must be an integer or b must be an integer')
    elif type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(b)
    else:
        return a + b
