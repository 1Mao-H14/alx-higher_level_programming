#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            v = ord(i) - 32
            print("{}".format(chr(v)), end="")
    print()
