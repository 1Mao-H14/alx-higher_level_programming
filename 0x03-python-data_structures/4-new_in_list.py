#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy_liste = my_list
        return copy_liste
    elif idx >= len(my_list):
        copy_liste = my_list
        return copy_liste
    else:
        newliste = list(my_list)
        newliste[idx] = element
        return newliste
