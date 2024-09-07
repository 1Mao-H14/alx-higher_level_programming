#!/usr/bin/python3
""" defines Rectangle class """


class Rectangle:
    """
    Class Rectangle that defines a rectangle
    Attributs:

        width (int): the width of the rectangle
        height (int): the height of the rectangle
        number_of_instances (int) : class attribut (the numbre of instance)
        print_symbol (int) : class attribut ( symbole used )


    """
    number_of_instances = 0
    print_syimbol = '#'

    def __init__(self, width=0, height=0):
        """
        initialising a new Rectangle
            Args:
                  width (int): the widht of the Rectangle
                  height(int) : the height of the Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    """ widht and height getter """
    @property
    def width(self):
        """
         the widht of the object
        Returns:
            int: the widht of the Rectangle object
        """
        return self.__width

    @property
    def height(self):
        """
        the height of the rectangle
        Returns:
            int : the height of the Rectangle object
        """
        return self.__height

    """ widht and height setter """
    @width.setter
    def width(self, value):
        """
        setting the widht value to an Rectangle object
        Args:
            value (int): the widht of the rectangle
        Raises:
            ValueError : if the value is < 0
            TypeError: if value is not an integer
        """
        if (type(value) is int):
            if (value >= 0):
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @height.setter
    def height(self, value):
        """
        setting the height value to an Rectangle object
        Args:
            value (int): the height of the rectangle
        Raises:
            ValueError : if the value is < 0
            TypeError: if value is not an integer
        """
        if (isinstance(value, int)):
            if (value >= 0):
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    def area(self):
        """
        Calculate the area of a Rectangle

        Returns:
             int : the area of a Rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of a Rectangle
        Returns:
             int : the perimeter of a Rectangle
        """
        if (self.__height == 0 or self.__width) == 0:
            return 0
        else:
            return (2*(self.__height + self.__width))

    def __str__(self):
        """
        printing the string

        Return:
            str : the string #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        c = ''
        for i in range(self.__height):
            for j in range(self.__width):
                c += str(self.print_symbol)
            c += '\n'
        return c.strip()

    def __repr__(self):
        """
        string representation of the rectangle to be able to recreate a new
        Returns:
            str : return a string representation of the rectangle
        """
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        """
        deleting the object

        Returns:
                nothing (NONE)
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
