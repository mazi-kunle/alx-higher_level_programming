#!/usr/bin/python3
'''This is a module'''


def read_file(filename=''):
    '''
    a function that reads a text file (UTF8)
    and prints it to stdout.
    '''
    with open(filename, 'r', encoding='Utf-8') as f:
        for line in f:
            print(line, end='')
