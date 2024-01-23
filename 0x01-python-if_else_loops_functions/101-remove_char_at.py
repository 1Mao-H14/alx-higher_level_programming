#!/usr/bin/python3
def remove_char_at(str, n):

    for i in range(len(str)):
        if i == n:
            sr = str[0:n] + str[n+1:]
            print(sr)
    if n < 0 or n >= len(str):
        print(str)
