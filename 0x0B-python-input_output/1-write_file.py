#!/usr/bin/python3

"""
A MODULE Thats containes read_file function
"""


sh: 1: q: not found
    """
    A Function that writes a string to returns the number of chars
    Args:

    filename(str): the file name
    text(str): texte entred

    Return:
        int : the length of the text file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
