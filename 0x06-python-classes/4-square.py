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
        self.size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')
