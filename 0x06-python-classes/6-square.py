#!/usr/bin/python3
'''that defines a square'''


class class Square:
    """
    A class used to represent a Square.

    ...

    Attributes
    ----------
    size : int
        the length of a side of the square (default is 0)
    position : tuple of int
        the position at which the square should be printed (default is (0, 0))

    Methods
    -------
    area()
        Returns the current square area.
    my_print()
        Prints the square with the character '#' at the specified position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size : int, optional
            The length of a side of the square (default is 0)
        position : tuple of int, optional
            The position whichthe square should be printed(default is (0,0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Gets or sets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """tuple: Gets or sets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if isinstance(value, tuple):
                if len(value) == 2:
                    if all(isinstance(i, int) for i in range(value)):
                        if all(i >= 0 for i in value):
                            self.__position = value
        except Exception:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """
        Returns the current square area.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' at the specified position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
