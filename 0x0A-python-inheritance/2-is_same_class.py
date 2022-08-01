#!/usr/bin/python3
'''This is a module'''


def is_same_class(obj, a_class):
    '''
    A function that rreturns True if the object is exactly an instance
    of the specified class.
    '''
    return (type(obj) == a_class)
