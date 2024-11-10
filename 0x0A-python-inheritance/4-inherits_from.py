#!/usr/bin/python3

"""4-inherits_from.py

This module defines a function `inherits_from` that checks if an object
is an instance of a class that inherits from a specified class. The
function returns `True` if the object is an instance of a subclass of
the specified class, but not an instance of the class itself. It returns
`False` if the object is not an instance of the specified class or any
subclass.

Functions:
    - inherits_from(obj, a_class): Returns True if the object is an
      instance of a subclass of a_class, otherwise False.
"""


def inherits_from(obj, a_class):

    """
    Returns True if obj is an instance of a subclass of a_class.
    Returns False if obj is not an instance or is an instance of
    a_class itself.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """

    if isinstance(obj, a_class):
        if ((type(obj) is not a_class) and (issubclass(type(obj), a_class))):
            return True
        return False
    else:
        return False
