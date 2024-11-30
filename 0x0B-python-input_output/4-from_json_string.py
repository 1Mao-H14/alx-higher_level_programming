#!/usr/bin/python3
"""
A MODULE Thats containes from_json_string function
"""


import json

def from_json_string(my_str):


    """
    a function that returns an object (Python data structure)
    represented by a JSON string
    Args:
        my_str (str): the string argument to be serialised
    Returns:
        object : an object
    """
    l_dile = json.loads(my_str)
    return l_dile
