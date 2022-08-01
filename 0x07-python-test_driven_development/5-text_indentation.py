#!/usr/bin/python3
'''This is a module'''


def text_indentation(text):
    '''
    a function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    '''
    if type(text) != str:
        raise TypeError('text must be a string')

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end='')
        if text[c] in '.?:':
            print('\n')

            while (c < len(text) - 1 and text[c + 1] == ' '):
                c += 1

            c += 1
        else:
            c += 1
