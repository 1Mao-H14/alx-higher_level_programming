#!/usr/bin/python3
"""
A MODULE Thats containes append_write function
"""


def append_write(filename="", text=""):
    """"
    append_write : that appends a string at the end of a text file

    Args:
        filename(str) : the file name
        text(str) : the text entred

    Return:
        int : the number of characters added
    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        wr_t = f.write(text)
        f.seek(0)
        ln_txt = len(f.read())
        return ln_txt
