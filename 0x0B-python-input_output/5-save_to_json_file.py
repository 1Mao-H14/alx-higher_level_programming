#!/usr/bin/python3

"""
A MODULE Thats containes A MODULE Thats containes
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    Args:
        my_obj (object): argument object
        filename (str): the file name
    Return:
        None : nothing
    """
    with open(filename, 'w', encoding='utf-8'):
        json.dump(my_obj, filename)

