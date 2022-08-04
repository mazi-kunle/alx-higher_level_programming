#!/usr/bin/python3
'''This is a module'''


class Student:
    '''A student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        A function that returns an instance attribute.
        '''
        new_dict = {}
        if (type(attrs) == list and all(isinstance(i, str) for i in attrs)):
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        '''
        A function that replaces all attributes of the Student instance:
        '''
        for key, value in json.items():
            setattr(self, key, value)
