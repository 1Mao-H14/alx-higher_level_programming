#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    new_tuple = ()
    for i in sentence:
        new_tuple += (i,)
        first_ele = new_tuple[0]
        return lenght, first_ele
    if new_tuple == ():
        new_tuple = new_tuple + (None,)
        first_ele = new_tuple[0]
    return lenght, first_ele
