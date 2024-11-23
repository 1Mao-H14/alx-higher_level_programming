#!/usr/bin/python3

"""
A MODULE Thats containes read_file function
"""


def write_file(filename="", text=""):
    """
    A Function that writes a string to a text file (UTF8) and returns the number of characters written:
    Args:

    filename(str): the file name
    text(str): texte entred

    Return:
        int : the length of the text file
    """
    with open(filename, mode = 'w', encoding = 'utf-8') as f:
        f.write(text)
        return len(text)
