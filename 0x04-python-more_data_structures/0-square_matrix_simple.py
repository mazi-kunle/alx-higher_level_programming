#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''
    A funcition that computes the square value of all integers of
    a matrix.
    '''
    new = []
    for i in matrix:
        new.append(list(map(lambda x: x**2, i)))
    return new
