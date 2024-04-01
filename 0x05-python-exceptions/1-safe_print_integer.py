#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(float(value)))
        return True
    except ValueError as e:
        return False
