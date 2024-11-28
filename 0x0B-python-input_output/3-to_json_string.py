#!/usr/bin/python3
"""A module that contains the to_json_string function."""
import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON string.

    Args:
        my_obj (object): The Python object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
