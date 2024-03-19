#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        sorted_keys = sorted(a_dictionary)
        list = []
        for i, v in a_dictionary.items():
            list.append(v)
        s_list = sorted(list)
        max_value = s_list[-1]
        return max_value
