#!/usr/bin/python3
head = 0
down = 0
def weight_average(my_list=[]):
    global head, down
    for i, v in (my_list):
        head += (i*v)
        down += v
        resulte = head/down
    return resulte
