#!/usr/bin/python3

"""
A MODULE Thats containes A MODULE Thats containes
"""
import json


def load_from_json_file(filename):
    """"
    a function that creates an Object from a “JSON file”
    Args:
        filename(str) : the name of the file (.json)
    Return:
        object: an object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
