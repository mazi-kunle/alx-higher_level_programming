#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    a function that replaces all occurences of an element
    by another in a new list.
    '''
    new = my_list.copy()
    return list(map(lambda x: replace if (x == search) else x, new))
