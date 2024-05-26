#!/usr/bin/python3
"""a class that defines a square
"""


class Square:
    """
    A class to represent a square.

    Attributes:
    -----------
    size : float or int
        The size of the sides of the square.

    Methods:
    --------
    area():
        Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size
        Parameters:
        -----------
        size : float or int, optional
            The size of the sides of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.
        Returns:
        --------
        float or int
            The size of the sides of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.
        Parameters:
        -----------
        value : float or int
            The size to set for the sides of the square.
        Raises:
        -------
        ValueError:
            If the size is less than or equal to 0.
        TypeError:
            If the size is not a number.
        """
        if isinstance(value, (int, float)):
            if value > 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be a number')

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        --------
        float or int
            The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Compare current square less than another square based on area
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """
        Compare  square is greater than another square based on area.
        """
        return self.area() > other.area()

    def __le__(self, other):
        """
        Compare square is less than or equal to another square based on area.
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """
        Compare   greater than or equal to another square area.
        """
        return self.area() >= other.area()

    def __eq__(self, other):
        """
        Compare square is equal to another square based on area.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare square is not equal to another square based on area.
        """
        return self.area() != other.area()
