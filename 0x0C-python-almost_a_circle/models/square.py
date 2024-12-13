#!/usr/bin/python3
""" A module which containes a square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.
        Args:
            value (int): width of square.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        msg = '[Square] ({:d}) {:d}/{:d} - {:d}'
        return msg.format(self.id, self.x, self.y, self.width)
