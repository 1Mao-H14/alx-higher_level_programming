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
        # validate width then instantate
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if (width <= 0):
            raise ValueError('width must be > 0')
        self.__width = width

        # validate height then instantate
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if (height <= 0):
            raise ValueError('height must be > 0')
        self.__height = height

        # validate x then instantate
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if (x < 0):
            raise ValueError('x must be >= 0')
        self.__x = x

        # validate y then instantate
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if (y < 0):
            raise ValueError('y must be >= 0')
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """int: Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """int: Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if (value <= 0):
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """int: x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if (value < 0):
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """int: y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for t in range(self.height):
            print(self.x * ' ' + self.width * '#')

    def __str__(self):
        msg = '[Rectangle] ({}) {}/{} - {}/{}'
        return msg.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ that assigns an argument to each attribute """
        if args:
            for (i, v) in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
        else:
            for i, v in kwargs.items():
                if i == 'id':
                    self.id = v
                elif i == 'width':
                    self.width = v
                elif i == 'height':
                    self.height = v
                elif i == 'x':
                    self.x = v
                elif i == 'y':
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
                }
