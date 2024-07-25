#!/usr/bin/python3
"""
A module for that printing a square with the character  # .
    Functions:
        print_square(size): print the a square with the character  #
"""


def print_square(size):
    """
    a function thats prints a square with the character #.
    Args:
    size(int): the size of rectangle
    Return:
        str : a square of # caracters
    Raises:
         TypeError : if size not an integer or its float
         ValueError: if size not >= 0
    """

    if (isinstance(size, float) and (size < 0)):
        raise TypeError('size must be an integer')
    elif not (isinstance(size, int)):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for h in range(size):
            for i in range(size):
                print('#', end='')
            print()
