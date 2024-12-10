#!/usr/bin/python3

"""Defines the Rectangle class, inheriting from Base."""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
            x (int): x-coordinate (default 0).
            y (int): y-coordinate (default 0).
            id (int, optional): Object ID.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """int: Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if (value <= 0):
            raise ValueError('width must be > 0')
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        self.__width = value

    @property
    def height(self):
        """int: Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if (value <= 0):
            raise ValueError('height must be > 0')
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        self.__height = value

    @property
    def x(self):
        """int: x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        if (value < 0):
            raise ValueError('x must be >= 0')
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        self.__x = value

    @property
    def y(self):
        """int: y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        if (value < 0):
            raise ValueError('y must be >= 0')
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        self.__y = value
