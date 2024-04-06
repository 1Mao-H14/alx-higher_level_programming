#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    v = 0
    for i in range(x):
        try:
            num = int(my_list[i])
            print("{:d}".format(num), end='')
            v += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
    print("")
    return v
