#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        s = (0, 0)
        tuple_a += s
        tuple_b += s
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
