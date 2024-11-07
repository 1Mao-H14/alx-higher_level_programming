#!/usr/bin/python3


"""
    A module thats containes the is_same_class function
    Function:
        is_same_class(obj, a_class) : returns if the object is exactly an instance of the 
        specified class ;otherwise False

"""


    def is_same_class(obj, a_class):


        """
        a function thats returns True if the object is exactly an 
        instance of the specified class 
        ; otherwise False.
        Args:
            obj(object): an object
            a_class(class) : a class
        Returns:
            True :if the object is exactly an instance of 
            the specified class . otherwise False.
        """

        return (isinstance(obj, a_class))
