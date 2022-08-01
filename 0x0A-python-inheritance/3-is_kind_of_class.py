#!/usr/bin/python3
'''This is a module'''


def is_kind_of_class(obj, a_class):
    '''
    A function that returns True if the object is exactly an instance
    of the specified class.
    '''
    return (isinstance(obj, a_class))
