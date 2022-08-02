#!/usr/bin/python3
'''This is a module'''


class MyInt(int):
    '''A class that inherits from int'''
    def __eq__(self, other):
        '''
        Override == opeartor with != behavior.
        '''
        return (self.real != other)

    def __ne__(self, other):
        '''
        Override != operator with == behavior.
        '''
        return (self.real == other)
