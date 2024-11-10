#!/usr/bin/python3
"""4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """ Check for direct or indirect inheritance """
    if isinstance(obj, a_class):
        if ((type(obj) != a_class) and (issubclass(type(obj), a_class)))
            return True
    else:
        return False
