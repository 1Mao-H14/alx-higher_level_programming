#!/usr/bin/python3

"""A Module which containes Rectangle class"""

from base import Base


class Rectangle(Base):
    """"A class thats represent a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super.__init__(id)

    # width getter property
    @property
    def width(self):
        self.__width

    # width setter
    @width.setter
    def width(self, value):
        self.__width = value

    # height getter
    @property
    def height(self):
        return self.__height

    # height setter
    @height.setter
    def height(self, value):
        self.__height = value

    # x getter
    @property
    def x(self):
        return self.__x

    # x setter
    @x.setter
    def x(self, value):
        self.__x = value

    # y getter
    @property
    def y(self):
        return self.__y

    # y setter
    @y.setter
    def y(self, value):
        self.__y = value
