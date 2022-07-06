#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''
    A function that retuens a set of all elements present
    in only one set.
    '''
    z = set_1.difference(set_2)
    y = set_2.difference(set_1)
    return z.union(y)
