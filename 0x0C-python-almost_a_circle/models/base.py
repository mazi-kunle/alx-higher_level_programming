#!/usr/bin/python3
'''This is a module'''


import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        '''
        return the list of the json string representation.
        '''
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set:
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            dummy_instance = Rectangle(1, 2)
        elif cls.__name__ == 'Square':
            dummy_instance = Square(2)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
        returns a list of instances:
        '''
        name_of_file = cls.__name__ + '.json'
        lst = []
        try:
            with open(name_of_file, 'r') as f:
                json_list = cls.from_json_string(f.read())

            for json_dict in json_list:
                instance = cls.create(**json_dict)
                lst.append(instance)

        except (FileNotFoundError):
            pass

        finally:
            return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        serialize a file in CSV.
        '''
        name_of_file = cls.__name__ + '.csv'

        with open(name_of_file, 'w', newline='') as f:
            if cls.__name__ == 'Rectangle':
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fieldnames = ['id', 'size', 'x', 'y']

            for instance in list_objs:
                instance_dict = instance.to_dictionary()
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writerow(instance_dict)

    @classmethod
    def load_from_file_csv(cls):
        '''
        deserialize a file in CSV.
        '''
        name_of_file = cls.__name__ + '.csv'
        lst = []

        with open(name_of_file, 'r') as f:
            if cls.__name__ == 'Rectangle':
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fieldnames = ['id', 'size', 'x', 'y']

            reader = csv.DictReader(f, fieldnames=fieldnames)
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['x'] = int(row['x'])
                    row['y'] = int(row['y'])
                    row['width'] = int(row['width'])
                    row['height'] = int(row['height'])

                except KeyError:
                    row['size'] = int(row['size'])

                finally:
                    instance = cls.create(**row)
                    lst.append(instance)

        return lst
