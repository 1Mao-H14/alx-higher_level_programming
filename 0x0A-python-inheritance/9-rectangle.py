#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""

# Importing BaseGeometry class from 7-base_geometry.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates that both width and height are positive integers.
        """
        self.integer_validator("width", width)  # Validates the width
        self.integer_validator("height", height)  # Validates the height
        self.__width = width  # Private attribute for width
        self.__height = height  # Private attribute for height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: String in the format "[Rectangle] width/height".
        """
        return f'[Rectangle] {self.__width}/{self.__height}'
