#!/usr/bin/python3
"""
A module that defines a Square class.
"""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """Initializes the Square with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        self.size = size  # Use the property setter for validation

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

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character.

        If the size is 0, it prints an empty line.
        Otherwise, it prints the square line by line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
