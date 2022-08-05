#!/usr/bin/python3
'''This is a module'''


def append_after(filename="", search_string="", new_string=""):
    '''
    a function that inserts a line of text to a file,
    after each line containing a specific string.
    '''
    with open(filename, 'r') as f:
        a = f.readlines()

    for i in a[:]:
        is search_String in i:
            line = a.index(i)
            a.insert(line, new_string)

    with open(filename, 'w') as f:
        f.writelines(a)
