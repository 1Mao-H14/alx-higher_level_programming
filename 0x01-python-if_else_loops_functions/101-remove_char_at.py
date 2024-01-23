#!/usr/bin/python3
def remove_char_at(s, n):
    for i in range(len(s)):
        if i == n:
            sr = s[0:i] + s[i+1:]
            print(sr)
    if n < 0 or n >= len(s):
        print(s)
