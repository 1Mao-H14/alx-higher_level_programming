#!/usr/bin/python3

"""a module which containes Base class"""


class Base:
    """A class which represent Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
