#!/usr/bin/python3
'''This is a module'''


def append_write(filename="", text=""):
    '''
    a function that appends a string at the end of
    a text file (UTF8) and returns the number of characters added:
    '''
    with open(filename, 'a', encoding='Utf-8') as f:
        return f.write(text)
