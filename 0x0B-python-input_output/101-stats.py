#!/usr/bin/python3

"""A module which contains a script that reads stdin
line by line and computes metrics"""

import sys
from collections import Counter

file = sys.stdin
list_val = []
size = 0
c = 0

try:
    for i in file:
        ln_val = i.strip().split()
        size += int(ln_val[-1])
        list_val.append(int(ln_val[-2]))
        c += 1

        if c == 10:  # Process a full batch of 10 lines
            c1 = Counter(list_val)
            map_val = dict(c1)
            sorted_key_map = sorted(map_val)

            print('File size: {:d}'.format(size))
            for s in sorted_key_map:
                print('{:d}: {:d}'.format(s, map_val[s]))

            # Reset counters for the next batch
            c = 0
            list_val = []

    # After the loop, handle any leftover lines
    if list_val:
        c1 = Counter(list_val)
        map_val = dict(c1)
        sorted_key_map = sorted(map_val)

        print('File size: {:d}'.format(size))
        for s in sorted_key_map:
            print('{:d}: {:d}'.format(s, map_val[s]))

except KeyboardInterrupt:
    # Handle any leftover lines before exiting
    if list_val:
        c1 = Counter(list_val)
        map_val = dict(c1)
        sorted_key_map = sorted(map_val)

        print('File size: {:d}'.format(size))
        for s in sorted_key_map:
            print('{:d}: {:d}'.format(s, map_val[s]))
