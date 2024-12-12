#!/usr/bin/python3
"""A module which containes a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square"""
    def __init__(size, x=0, y=0, id=None):
        super().__init__(self, width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        msg = '[Square] ({:d}) {:d}/{:d} - {:d}'
        return msg.format(self.id, self.x, self.y, self.width)
