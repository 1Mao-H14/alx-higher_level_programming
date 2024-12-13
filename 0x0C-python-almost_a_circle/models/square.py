#!/usr/bin/python3
""" A module which containes a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        msg = '[Square] ({:d}) {:d}/{:d} - {:d}'
        return msg.format(self.id, self.x, self.y, self.width)
