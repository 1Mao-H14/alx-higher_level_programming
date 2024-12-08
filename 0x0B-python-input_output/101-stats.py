#!/usr/bin/python3

""""A module which containes a script that reads stdin line by line and computes metrics:"""


from sys import stdini
from collections import Counter


file = stdin
lines = file.readlines()
list_val = []
size = 0
c = 0
try:
    for i in lines:
        if c < 10:
            ln_val = i.strip().split()
            size += int(ln_val[-1])
            list_val.append(int(ln_val[-2]))
            c += 1
    c1 = Counter(list_val)
    # sorting the dict
    map_val = dict(c1)
    sorted_key_map = sorted(map_val)
    new_sorted = {}
    for e in sorted_key_map:
        new_sorted[e] = map_val[e]

    c = 0
    print('File size: {:d}'.format(size))
    for s, c in new_sorted.items():
        print('{:d}: {:d}'.format(s, c))

except KeyboardInterrupt:
    c = 0
    print('File size: {:d}'.format(size))
