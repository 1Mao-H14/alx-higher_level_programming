#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j * j)
        new_list.append(row)
    return new_list
