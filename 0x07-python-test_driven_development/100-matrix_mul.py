#!/usr/bin/python3
"""
a mudule thats do  matrix multiplication
    Functions:
        matrix_mul(m_a, m_b): a function thats multiplies two matrix
"""


def matrix_mul(m_a, m_b):
    """
    A function thats multiply two matrixs
    Args:
        m_a(list): the first list
        m_b(list): the second list
    Returns:
         multipled matrix(list)
    Raises:
        TypeError : if m_a or m_b is not a list or m_a or m_b not a
                    if not containes integers or floats
        ValueError : if m_a or m_b is empty or cant be multiplied

    """
    # m_a and m_b must be an list of lists of integers or floats
    # must be a list or m_b must be a list
    # if m_a or m_b is not a list: raise a TypeError exception with message m_a
    if not (isinstance(m_a, list)):
        raise TypeError('m_a must be a list')
    if not (isinstance(m_b, list)):
        raise TypeError('m_b must be a list')
    # if m_a or m_b is not a list of lists: raise a TypeError exception with
    # message m_a must be a list of lists or m_b must be a list of
    # lists

    if not all((isinstance(i, list) for i in m_a)):
        raise TypeError('m_a must be a list of lists')

    if not all((isinstance(i, list) for i in m_b)):
        raise TypeError('m_b must be a list of lists')

    if (len(m_a) == 0) or (any(len(j) == 0 for j in m_a)):
        raise ValueError("m_a can't be empty")

    if (len(m_b) == 0) or (any(len(j) == 0 for j in m_b)):
        raise ValueError("m_b can't be empty")

    for j in m_a:
        for e in j:
            if not(isinstance(e, (int, float))):
                raise TypeError('m_a should contain only integers or floats')

    for j in m_b:
        for e in j:
            if not(isinstance(e, (int, float))):
                raise TypeError('m_b should contain only integers or floats')

    # same size or each row of m_b must be of the same size

    for i in range(len(m_a)-1):  # [[][][]]
        if len(m_a[i]) != len(m_a[i+1]):
            raise TypeError('each row of m_a must be of the same size')
    for i in range(len(m_b) - 1):
        if len(m_b[i]) != len(m_b[i+1]):
            raise TypeError('each row of m_b must be of the same size')

    # multiplication
    rows_A = len(m_a)
    cols_A = len(m_a[0])
    rows_B = len(m_b)
    cols_B = len(m_b[0])
    erure = "m_a and m_b can't be multiplied"
    if cols_A != rows_B:
        raise ValueError(erure)

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform the multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
