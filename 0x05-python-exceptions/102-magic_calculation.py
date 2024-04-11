#!/usr/bin/python3
def magic_calculation(a, b):
    retry = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            retry += a ** b / i
        except Exception:
            retry = b + a
            break
    return retry
