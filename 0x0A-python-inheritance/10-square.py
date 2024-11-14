#!/usr/bin/python3
"""Square class that inherits from Rectangle.

Defines the `Square` class, a subclass of `Rectangle`
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.

    Inherits from `Rectangle` with `size` as both width and height.

    Args:
        size (int): Side length of the square.
    """

    def __init__(self, size):
        """Initialize the square.

        Validates `size` and initializes the parent `Rectangle`.

        Args:
            size (int): Side length of the square.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the square's area.

        Returns:
            int: Area (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """String representation of the square.

        Returns:
            str: "[Rectangle] size/size".
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
