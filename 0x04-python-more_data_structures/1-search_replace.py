#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for e in my_list:
        new_list.append(e)
        if (e == search):
            new_list.remove(e)
            new_list.insert(len(my_list), replace)
        else:
            continue
    return new_list
