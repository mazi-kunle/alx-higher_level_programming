#!/usr/bin/python3
'''This is a module'''


import sys
import json

load_from_json_file = __import__('6-load_from_json_file'). load_from_json_file

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

lst = sys.argv[1:]

try:
    load_from_json_file = load_from_json_file('add_item.json')

except (FileNotFoundError):
    save_to_json_file(lst, 'add_item.json')

else:
    load_from_json_file.extend(lst)
    save_to_json_file(load_from_json_file, 'add_item.json')
