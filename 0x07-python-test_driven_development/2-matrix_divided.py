#!/usr/bin/python3
""" matrix_divided
A module thats devide integer of a matrix
    Function:
        matrix_divided(matrix, div): a function that divides
        all elements of a matrix.

"""


def matrix_divided(matrix, div):
    erure = 'matrix must be a matrix (list of lists) of integers/floats'
    """function thats devides integrs of matrix

        matrix ( ist) : the matrix
        div (float) : the integr to be devided
    
    Returns:
        new matrix of devide integrs

    Raises:
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        ZeroDivisionError: division by zero

    """
    for le in range(len(matrix) - 1):
        if len(matrix[le]) != len(matrix[le + 1]):
            raise TypeError('Each row of the matrix must have the same size')
    ls2 = []
    if not(isinstance(matrix, list)):
        raise TypeError(erure)
    else:
        for i in matrix:
            ls1 = []
            if not(isinstance(i, list)):
                raise TypeError(erure)
            else:
                for j in i:
                    if not(isinstance(j, (float, int))):
                        raise TypeError(erure)
                    else:
                        if (div == 0):
                            raise ZeroDivisionError('division by zero')
                        else:
                            n = float(j / div)
                            val = round(n, 2)
                            ls1.append(val)
            ls2.append(ls1)
        return ls2
