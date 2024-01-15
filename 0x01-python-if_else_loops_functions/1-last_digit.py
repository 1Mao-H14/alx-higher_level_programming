#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number / 10
if ld > 5:
    print("Last digit of {number} is {ld} {} and is greater than 5")
