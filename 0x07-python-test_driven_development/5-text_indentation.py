#!/usr/bin/python3
'''This is a module'''


def text_indentation(text):
    '''
    a function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    '''
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end='')
        if text[c] in '.?:':
            print('\n')
            c += 2
            continue
        else:
            c += 1
