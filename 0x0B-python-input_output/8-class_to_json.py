#!/usr/bin/python3
""" A module thats containes class_to_json
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with
    simple data structure for JSON serialization of an object
    """
    return obj.__dict__