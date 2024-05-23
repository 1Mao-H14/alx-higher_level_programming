#!/usr/bin/python3
"""
A module that defines a Square class.
"""


class Square:

    """A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes the Square with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """

        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
