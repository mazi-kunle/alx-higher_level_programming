#!/usr/bin/python3
'''This is a module'''


def text_indentation(text):
    '''
     a function that prints a text with 2 new lines after
     each of these characters: ., ? and :
     '''
     for i in text:
         if i in '.,?:':
             print(i, end='')
             print('\n')
             print(
         else:
             print(i, end='')
