#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    '''
    A function that returns a list with all values multiplied by
    a number without using any loops.
    '''
    new = my_list.copy()
    return list(map(lambda x: x*number, new))
