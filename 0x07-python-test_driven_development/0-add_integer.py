#!/usr/bin/python3
""" A module thats adds integrs
Functions:
    add_integer(a, b): a function thats returns the sum of a and b

"""


def add_integer(a, b=98):
    """
    a function thats add two numbers and casting before adding

    Args:
        a(int):the first number
        b(int):the second number
    Return:
        int : the resulte of the sum of a and  b
    Raises:
        TypeError : a must be an integer or b must be an integer

    """

    if((isinstance(a, (float, int))) and
            (isinstance(b, (float, int))) is True):
        return (int(a) + int(b))
    elif ((isinstance(a, (float, int))) is False):
        raise TypeError('a must be an integer')
    elif ((isinstance(b, (float, int))) is False):
        raise TypeError('b must be an integer')
