#!/usr/bin/python3

# Dynamically import BaseGeometry from '7-base_geometry.py'
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""8-rectangle.py
This module defines a Rectangle class that inherits from BaseGeometry.
"""

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.
    Validates width and height using integer_validator from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (positive integer).
            height (int): The height of the rectangle (positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        super().integer_validator("width", width)  # Validate width
        super().integer_validator("height", height)  # Validate height
        
        self.__width = width  # Private width attribute
        self.__height = height  # Private height attribute
