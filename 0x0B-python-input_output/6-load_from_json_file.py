#!/usr/bin/python3
'''This is a module'''

import json


def load_from_json_file(filename):
    '''
    a function that creates an Object from a “JSON file”:
    '''
    with open(filename, 'r', encoding='Utf-8') as f:
        return json.load(f)
