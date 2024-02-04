#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    else:
        for i in range(len(argv)):
            if i == 0:
                print("{} arguments:".format(len(argv) - 1))
                continue
            else:
                print("{}: {}".format(i, argv[i]))
