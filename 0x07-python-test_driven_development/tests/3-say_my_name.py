#!/usr/bin/python3
'''This is a module'''


def say_my_name(first_name, last_name=""):
    '''
    a function that prints My name is <first name> <last name>
    '''
    if (type(firstname) != str):
        raise TypeError('first_name must be a string')
    elif (type(lastname) != str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
