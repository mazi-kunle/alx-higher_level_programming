#!/usr/bin/python3
'''This is a module'''


import json


class Base:
    '''
    This is a base class.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns the JSON string representation of list_dictionaries.
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        A function writes the JSON string representation
        of list_objs to a file:
        '''
        name_of_file = cls.__name__ + '.json'
        d = []
        if list_objs is not None:
            for i in list_objs:
                i = i.to_dictionary()
                json_dict = json.loads(cls.to_json_string(i))
                d.append(json_dict)

        with open(name_of_file, 'w') as f:
            json.dump(d, f)
