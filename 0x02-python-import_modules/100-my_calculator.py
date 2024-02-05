#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        module = argv[2]
        if module not in ('+', '-', '*', '/'):
            print("Unknown operator. Available operators: +, -, *, and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            print("{} {} {}".format(a, module, b))
