#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary.copy():
        if (a_dictionary.copy()[i] == value):
            del a_dictionary[i]
    return a_dictionary
