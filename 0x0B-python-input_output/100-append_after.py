#!/usr/bin/python3

""""A module which containes student class and append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after lines containing a specific
    search string in a file.

    Args:
        filename (str): Name of the file to modify.
        search_string (str): String to search for in the file's lines.
        new_string (str): String to append after matching lines.
    Return:
        none : nothing
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='utf-8') as w:
        for line in lines:
            w.write(line)
            if search_string in line:
                w.write(new_string)
            else:
                pass
