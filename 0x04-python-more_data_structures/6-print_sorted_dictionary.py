#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_dict = a_dictionary.keys()
    sort_dict = sorted(key_dict)
    for e in sort_dict:
        print("{}: {}".format(e, a_dictionary[e]))
