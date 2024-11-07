#!/usr/bin/python3


"""2-is_same_class.py
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
