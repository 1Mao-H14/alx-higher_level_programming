#!/usr/bin/python3

"""
4-inherits_from.py

"""


def inherits_from(obj, a_class):
    """
    a function thats  returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    Args:
        obj(object): argument object
        a_class(class): argument class
    Return:
        True : if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class
        False : if not
    """
    if isinstance(obj, a_class):
        if ((type(obj) != a_class) and (issubclass(type(obj), a_class)))
            return True
    else:
        return False
