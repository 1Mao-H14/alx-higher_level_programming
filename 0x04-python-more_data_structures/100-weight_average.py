#!/usr/bin/python3
def weight_average(my_list=[]):
    head = 0
    down = 0
    if my_list == []:
        down = 1
    for i, v in my_list:
        head += (i * v)
        down += v
    resulte = head / down
    return resulte
