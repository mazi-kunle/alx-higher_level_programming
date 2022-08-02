#!/usr/bin/python3
'''This is a module'''


def add_attribute(obj, attr, name):
    '''
    a function that adds a new attribute
    to an object if it’s possible.

    '''
    if (not isinstance(obj, object)):
        raise TypeError("can't add new attribute")

    obj.attr = name
