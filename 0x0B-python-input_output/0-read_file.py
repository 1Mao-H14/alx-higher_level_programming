#!/usr/bin/python3

"""
A MODULE Thats containes read_file function
"""


def read_file(filename=""):
    """
    A Function that reads a text file (UTF8) and prints it to stdout:
    filename(str): the file name

    Return:
        None : nothing
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        f_read = f.read()
        print(f_read, end='')
