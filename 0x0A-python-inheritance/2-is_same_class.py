#!/usr/bin/python3

"""
Module for checking if an object is exactly an instance of a specified class.

Function:
    is_same_class(obj, a_class) -> bool:
        Returns True if the object is exactly an
    instance of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare the object against.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
