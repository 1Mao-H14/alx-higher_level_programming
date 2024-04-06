#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resulte = a / b
    except ZeroDivisionError:
        resulte = None
    finally:
        print("Inside result: {}".format(resulte))
        return resulte
