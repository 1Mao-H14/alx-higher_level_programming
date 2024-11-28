#!/usr/bin/python3
"""A module which contanes the append_write function"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    Args:
        filename(str): the file name
        text (str) : the text written
    Returns:
        int : the numbers of text appended"""
    with open(filename, 'a+', encoding = 'utf-8') as f:
        f.write(text)
    return len(text)
