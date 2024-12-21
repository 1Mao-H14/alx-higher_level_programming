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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        if args:
            for (i, v) in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
        else:
            for i, v in kwargs.items():
                if i == 'id':
                    self.id = v
                elif i == 'size':
                    self.size = v
                elif i == 'x':
                    self.x = v
                elif i == 'y':
                    self.y = v

    def __str__(self):
        msg = '[Square] ({:d}) {:d}/{:d} - {:d}'
        return msg.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the object.

        Parameters:
        - *args: Positional arguments to update
        attributes in the order ['id', 'size', 'x', 'y'].
        - **kwargs: Keyword arguments
        to update attributes by name.

        Behavior:
        - If `args` is non-empty,
        updates attributes based on their order.
        - If `args` is empty, updates
        attributes based on `kwargs` keys.
        """
        ls_ele = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for e in range(len(args)):
                setattr(self, ls_ele[e], args[e])
        else:
            for e in ls_ele:
                if e in kwargs:
                    setattr(self, e, kwargs[e])

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'size': self.__width,
            'x': self.__x,
            'y': self.__y
            }
