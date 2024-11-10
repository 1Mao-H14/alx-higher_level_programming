#!/usr/bin/python3
BaseGeometry = __import__(7-base_geometry.py).BaseGeometry

""" A Module thats containes Rctangle class
"""


class Rectangle(BaseGeometry):

    """A class thats represent A Rectangle
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
