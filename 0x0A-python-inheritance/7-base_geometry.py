#!/usr/bin/python3
"""A Module that's containes BaseGeometry
"""


class BaseGeometry:

    """ BaseGeometry class """

    def integer_validator(self, name, value):

        """a function thats returns type TypeError or ValueError
        exception depending on the value entred
        Args:
            name(str): name argument
            value(st) : value arguement
        Return:
            None: besicaly nothing
        Raises:
            TypeError : if value is not an integer
            ValueError : if value is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif (value <= 0):
            raise ValueError('{} must be greater than 0'.format(name))

    def area(self):
        """ raises an Exception """
        raise Exception('area() is not implemented')
