#!/usr/bin/python3
"""
A Module that adds all arguments to a Python list, and then save them to a file

This script adds command-line arguments to a list stored in a file called
`add_item.json`. If the file does not exist, it initializes an empty list.
The new arguments are appended to the list, and the updated list is saved
back to the file in JSON format.

Functions:
- load_from_json_file: Loads a Python object from a JSON file.
- save_to_json_file: Saves a Python object to a JSON file.
"""


import os
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'
if os.path.exists(filename):
    l_list = load_from_json_file(filename)
else:
    l_list = []
valid_list = l_list + argv[1:]

save_to_json_file(valid_list, filename)
