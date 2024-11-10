#!/usr/bin/python3

"""
4-inherits_from.py

This script defines a function `inherits_from` that checks if an object is an 
instance of a class that inherits from a specified class (but not the class itself).

Function:

- inherits_from(obj, a_class):
    Returns `True` if `obj` is an instance of a class that inherits from `a_class`,
    and `False` if it is either not an instance or is exactly an instance of `a_class`.

Args:
    obj (object): The object to check.
    a_class (class): The class to check against.

Returns:
    bool: True if `obj` is an instance of a subclass of `a_class` but not `a_class` itself.
"""

def inherits_from(obj, a_class):
    """
    Returns True if `obj` is an instance of a subclass of `a_class`, but not `a_class` itself.
    """
    if isinstance(obj, a_class):
        return type(obj) != a_class and issubclass(type(obj), a_class)
    return False
