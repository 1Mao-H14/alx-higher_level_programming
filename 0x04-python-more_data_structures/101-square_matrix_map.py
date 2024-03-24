#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    NewMatrix = map(lambda w: (list(map(lambda x: x**2, w))) , matrix)
    return list(NewMatrix)
