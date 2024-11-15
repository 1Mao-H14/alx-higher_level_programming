#!/usr/bin/python3

# Importing the Rectangle class from an external file

Rectangle = __import__('10-square.py').Rectangle

"""
Square class that inherits from Rectangle.

Defines the `Square` class, which represents a square and inherits
from the `Rectangle` class. The Square class ensures that both width
and height are the same, as required for a square.
"""

class Square(Rectangle):
    """Represents a square, a specific type of rectangle where width == height.

    Inherits from `Rectangle` but only requires one parameter: `size` for both
    width and height.

    Args:
        size (int): The side length of the square.
    """

    def __init__(self, size):
        """Initialize the square.

        Validates `size` and initializes the parent `Rectangle` class with the
        same value for width and height.

        Args:
            size (int): The side length of the square.
        """
        # Validate size using the parent class's integer_validator method
        super().integer_validator('size', size)

        # Set the private attribute for size
        self.__size = size

        # Initialize the parent Rectangle class with the size for both width and height
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area (size * size), which is the same for a square.
        """
        # Return the area of the square using the size
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: String in the format "[Square] size/size", which includes the
                 size of the square.
        """
        # Return a string representation of the square
        return "[Square] {}/{}".format(self.__size, self.__size)
