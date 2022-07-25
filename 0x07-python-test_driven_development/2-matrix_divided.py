#!/usr/bin/python3
'''This is a module'''

def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix.
    '''
    if (not all([isinstance(i, int) for j in matrix for i in j]) and
            not all(isinstance(i, float) for j in matrix for i in j])):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if for i i

