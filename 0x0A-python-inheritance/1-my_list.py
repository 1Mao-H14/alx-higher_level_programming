#!/usr/bin/python3

""" A module thats containes the sorting function
Classes:
    classe thats represent a a list
Function:
    print_sorted(self): return's sorted list
"""


class MyList(list):
    """
    classe thats represnt a list

        Attributes:(no attributes)
        Methods:
            print_sorted(self):return's the sorted list
            """
    def print_sorted(self):
        return self.sort()
