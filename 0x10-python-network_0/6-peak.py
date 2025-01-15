#!/usr/bin/python3
"""Module that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """
    Finds a peak element in a list of integers. A peak is an element that is greater than its neighbors.

    Parameters:
    - list_of_integers (list): A list of integers.

    Returns:
    - int: A peak element. If the list is empty, returns `None`.

    Uses binary search for O(log n) time complexity.

    Example:
    >>> find_peak([1, 3, 20, 4, 1])
    20
    >>> find_peak([1, 2, 3, 4, 5])
    5
    """
    ls = list_of_integers
    if ls == []:
        return None
    length = len(ls)

    s = 0
    e = length - 1
    while s < e:
        between = s + (e - s) // 2
        if ls[between] > ls[between - 1] and ls[between] > ls[between + 1]:
            return ls[between]
        if ls[between - 1] > ls[between + 1]:
            end = between
        else:
            s = between + 1
    return ls[s]
