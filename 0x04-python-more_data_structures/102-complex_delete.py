#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    idx_dic = {}
    for j, x in a_dictionary.items():
        idx_dic[j] = x
    for i, v in idx_dic.items():
        if v == value:
            del a_dictionary[i]
    return a_dictionary
