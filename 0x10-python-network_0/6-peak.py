#!/usr/bin/python3
'''This is a module'''
def find_peak(lst):
    '''
    A function that finds a peak in a list of unsorted integers
    '''
    start = 0
    end = len(lst)
    mid = (start + end) // 2
    if (len(lst) == 2):
        return max(lst[start], lst[end - 1])

    if (lst[mid] > lst[mid + 1] and lst[mid] > lst[mid - 1]):
        return lst[mid]

    if (lst[mid - 1] > lst[mid + 1]):
        return find_peak(lst[:mid+1])

    elif (lst[mid + 1]  > lst[mid - 1]):
        return find_peak(lst[mid+1::])


lst = [11,10,9,4,5,1,7]
a = find_peak(lst)
print(a)
