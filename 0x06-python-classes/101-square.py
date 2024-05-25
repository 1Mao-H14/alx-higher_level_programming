#!/usr/bin/python3
"""
A module that defines a Square class.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square with the character '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructs all the necessary attributes for the square object.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) for i in value) and
                all(i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    # publique area methode :
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    # publique print methode :
    def my_print(self):
        """
        Prints the square with the character '#'.

        If size is 0, it prints an empty line.
        The position by print the appropriate number of spaces, newlines.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print((self.__position[0] * ' ') + ('#' * self.__size))

    def __str__(self):
        """
        Returns a string representation of the square for printing.

        The string is formatted to match the output of the my_print method.

        Returns:
            str: The string representation of the square.
        """
        if self.__size == 0:
            return '\n'
        result = ''
        for _ in range(self.__position[1]):
            result += '\n'
        for _ in range(self.__size):
            result += (self.__position[0] * ' ') + ('#' * self.__size) + '\n'
        return result.rstrip()
