#!/usr/bin/python3
'''This is a module'''


class LockedClass:

    '''
    a class LockedClass with no class or object attribute,that
    prevents the user from dynamically creating new instance
    attributes,except if the new instance attribute is called first_name.
    '''
    def __init__(self):
        '''An init function'''
        pass

    def __setattr__(self, attribute, value):
        '''A custom setattr function'''
        if attribute != 'first_name':
            raise AttributeError('')
        else:
            self.__dict__[attribute] = value
