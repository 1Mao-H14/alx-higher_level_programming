#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as ze:
        print("Exception:", ze)
        return None
    except IndexError as ie:
        print("Exception:", ie)
        return None
