#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(values):
    """
    Finds a peak element in a list of integers. A peak is an element that.

    Parameters:
    - values (list): A list of integers.

    Returns:
    - int: A peak element. If the list is empty, returns `None`.

    Uses binary search for O(log n) time complexity.

    Example:
    >>> find_peak([1, 3, 20, 4, 1])
    20
    >>> find_peak([1, 2, 3, 4, 5])
    5
    """
    if not values:
        return None
    total_elements = len(values)

    left_index, right_index = 0, total_elements - 1
    while left_index < right_index:
        middle_index = left_index + (right_index - left_index) // 2
        if values[middle_index] > values[middle_index - 1] and
        values[middle_index] > values[middle_index + 1]:
            return values[middle_index]
        if values[middle_index - 1] > values[middle_index + 1]:
            right_index = middle_index
        else:
            left_index = middle_index + 1
    return values[left_index]
