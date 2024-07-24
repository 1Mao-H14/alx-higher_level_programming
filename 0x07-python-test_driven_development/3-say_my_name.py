#!/usr/bin/python3
"""
A module thats thats print strings
    Functions:
        say_my_name(first_name, last_name=""): a function thats print name last name
"""
def say_my_name(first_name, last_name=""):
    """
    A function thats prints My name is <first name> <last name>
    Args:
        first_name(str): the first string
        last_name(str): the second string
    Returns:
        return nothing
    Raises:
        TypeError: in case of the first_name or the first string is not string 

    """
    if not(isinstance(first_name, str)):
        raise TypeError('first_name must be a string')
    elif not(isinstance(last_name, str)):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
