#!/usr/bin/python3

def weight_average(my_list=[]):
    '''
    A function that returns the weighted average of all
    integers tuple.
    '''
    if len(my_list) == 0:
        return 0
    summ = 0
    sum2 = 0
    for i in my_list:
        mul = i[0] * i[1]
        summ = summ + mul
        sum2 = sum2 + i[1]
    return summ / sum2
