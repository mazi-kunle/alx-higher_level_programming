#!/usr/bin/python3
'''This is a module'''


def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix.
    '''
    if (matrix == [] or not all([isinstance(row, list) for row in matrix])):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    elif (not all([isinstance(i, int) for j in matrix for i in j]) and
            not all([isinstance(i, float) for j in matrix for i in j])):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    elif not all([len(matrix[0]) == len(i) for i in matrix]):
        raise TypeError('Each row of the matrix must have the same size')

    elif type(div) != int and type(div) != float:
        raise TypeError('div must be a number')

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x/div, 2), row)) for row in matrix])
