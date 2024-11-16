#!/usr/bin/python3
"""
Module to dynamically add an attribute to an object.

This module defines a function `add_attribute` that attempts to add a new
attribute to an object if the object is mutable. If the object is of an
immutable type (such as int, str, tuple, or float) or a subclass of these
types, a TypeError is raised.

The `add_attribute` function can be used to modify objects at runtime by
adding new attributes to them.

Usage Example:
    class MyClass:
        pass
    my_obj = MyClass()
    add_attribute(my_obj, "name", "John")
    print(my_obj.name)  # Outputs: John
"""


def add_attribute(obj, att, val):
    """
    Adds a new attribute to an object if allowed.

    This function sets the attribute `att` to the value `val` on the object
    `obj`. Raises a `TypeError` if the object is of an immutable type (int,
    str, tuple, float) or its subclass.

    Args:
        obj (object): The object to modify.
        att (str): The name of the attribute.
        val (any): The value to assign to the attribute.

    Raises:
        TypeError: If the object is immutable or its subclass.

    Example:
        class MyClass:
            pass
        my_obj = MyClass()
        add_attribute(my_obj, "name", "John")
        print(my_obj.name)  # Outputs: John
    """
    if isinstance(obj, (int, str, tuple, float)):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
