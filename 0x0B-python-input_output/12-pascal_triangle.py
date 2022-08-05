#!/usr/bin/python3
'''This is a module'''


def factorial(n):
    '''
    returns the factorial of n.
    '''
    if (n < 1):
        return 1
    return n * factorial(n - 1)


def pascal_triangle(n):
    '''
    A function that returns a list of lists of integers representining
    the pascal"s triangle of n.
    '''
    if (n <= 0):
        return []

    final = []
    lst = []
    for i in range(n):
        for j in range(i + 1):
            a = factorial(i) // (factorial(i-j) * factorial(j))
            lst.append(a)
        final.append(lst)
        lst = []
    return final
