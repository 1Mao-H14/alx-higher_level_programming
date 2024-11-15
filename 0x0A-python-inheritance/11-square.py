#!/usr/bin/python3
Rectangle = __import__('10-square.py').Rectangle

"""Square class that inherits from Rectangle.

Defines the `Square` class, which represents a square and inherits
"""


class Square(Rectangle):
    """Represents a square.

    Inherits from `Rectangle` but only requires one parameter: `size` for both
    width and height.

    Args:
        size (int): The side length of the square.
    """

    def __init__(self, size):
        """Initialize the square.

        Validates `size` and initializes the parent `Rectangle`

        Args:
            size (int): The side length of the square.
        """
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: String in the format "[Rectangle] size/size".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
