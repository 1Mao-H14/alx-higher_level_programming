#!/usr/bin/python3
for v in range(ord('z'), ord('a') - 1, -1):
    if v % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(v - diff)), end='')

