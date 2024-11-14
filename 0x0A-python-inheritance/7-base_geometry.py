#!/usr/bin/python3
"""A Module that's containes BaseGeometry 
"""


class BaseGeometry:
    """ BaseGeometry class """
    def integer_validator(self, name, value):
        """ """
        if type(self.value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        elif (self.value <= 0):
            raise ValueError('{} must be greater than 0')
    def area(self):
        """ raises an Exception """
        raise Exception('area() is not implemented')
