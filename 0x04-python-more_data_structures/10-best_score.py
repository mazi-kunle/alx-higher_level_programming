#!/usr/bin/python3

def best_score(a_dictionary):
    '''
    A function that returns a key with the biggest integer value.
    '''
    if a_dictionary is None:
        return None
    elif len(a_dictionary) == 0:
        return None

    key = a_dictionary[0]
    for i in a_dictionary:
        if a_dictionary[i] > key:
            key = a_dictionary[i]

    return key
