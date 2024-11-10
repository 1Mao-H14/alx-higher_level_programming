#!/usr/bin/python3

"""
A Module thats containes is_kind_of_class(obj, a_class) function
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
    if type(obj) != a_class:
        return True
    else:
        return False
