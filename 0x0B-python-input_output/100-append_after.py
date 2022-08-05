#!/usr/bin/python3
'''This is a module'''


def append_after(filename="", search_string="", new_string=""):
    '''
    a function that inserts a line of text to a file,
    after each line containing a specific string.
    '''
    with open(filename, 'r') as f:
        a = f.readlines()
    
    line = 0
    for i in a[:]:
        if search_string in i:
            line += 1
            a.insert(line, new_string)
        line += 1
        
    with open(filename, 'w') as f:
        f.writelines(a)
