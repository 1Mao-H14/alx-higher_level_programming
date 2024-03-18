#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for i, v in a_dictionary.items():
        mul = v*2
        new_dic[i] = mul
    return new_dic
