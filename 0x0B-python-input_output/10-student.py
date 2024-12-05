#!/usr/bin/python3
class Student():
    """"class thats represent Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name  # Assign the first name to the instance
        self.last_name = last_name    # Assign the last name to the instance
        self.age = age                # Assign the age to the instance

    def to_json(self, attrs=None):
        """
        Retrieves the dictionary representation of a Student instance.

        If `attrs` is provided, only the attributes specified in `attrs` are returned.
        all attributes must be retrieved.

        Args:
            attri (str) : the attribute to get 

        Returns:
            dict: if is a list of strings, only attribute names contained in this list must be retrieved. in 
            a dictionary representation
            else attributes must be retrieved
        """
        if isinstance(attrs, list):
            # Initialize an empty dictionary to store the selected attributes
            di = {}
            # Loop over the list of attribute names passed in attrs
            for e in attrs:
                # Check if e is a string and if the attribute exists in the instance
                if isinstance(e, str) and hasattr(self, e):
                    di[e] = getattr(self, e)  # Add the attribute and its value to the dictionary
            return di
        else:
            # If no attrs are provided, return all attributes of the student instance
            return self.__dict__
