#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible:
Raise a TypeError exception, with the message can't add new attribute
"""


def add_attribute(obj, att, val):
    """
    Adds an attribute to an object if allowed.

    This function adds a new attribute `att` with value `val` to `obj.
    a `TypeError` if the object is immutable (int, str, tuple, float)
    class defines `__slots__` and does not allow the attribute.

    Args:
        obj: The object to modify.
        att: The name of the attribute to add.
        val: The value of the attribute.

    Raises:
        TypeError: If the object is immutable or if the attribute

    Example:
        class MyClass: pass
        obj = MyClass()
        add_attribute(obj, "name", "Alice")
        print(obj.name)  # Outputs: Alice
    """
    if isinstance(obj, (int, str, tuple, float)):
        raise TypeError("can't add new attribute")
            print('first loop')
    if hasattr(obj.__class__, '__slots__') and ( att not in type(obj).__slots__ ):
        raise TypeError("can't add new attribute")
            print('second loop')
    setattr(obj, att, val)
