#!/usr/bin/python3
'''This is a module'''


def add_attribute(obj, attr, name):
    '''
    a function that adds a new attribute
    to an object if it’s possible.

    '''
    if (not hasattr(obj, '__dict__')):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, name)
