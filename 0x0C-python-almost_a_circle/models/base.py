#!/usr/bin/python3
import os
import json

"""a module which containes Base class"""


class Base:
    """A class which represent Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A fucntion that returns the JSON string representation
        of list_dictionaries"""
        import json
        if not list_dictionaries:
            return "[]"
        val = json.dumps(list_dictionaries)
        return val

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of `list_objs` to a file.

        Args:
            list_objs (list): List of objects, each having a `to_dictionary()` method.
        
        Creates or overwrites a file named `<ClassName>.json` with the JSON data.
        If `list_objs` is None, writes an empty list (`[]`).
        """
        from models.square import Square

        if issubclass(cls, Base):
                name = '{}.json'.format(cls.__name__)
                if os.path.exists(name):
                    f = open(name, 'a', encoding='utf-8')
                else:
                    f = open(name, 'w', encoding='utf-8')
                if list_objs is not None:
                    arr = []
                    for i in list_objs:
                        d_v = i.to_dictionary()
                        arr.append(d_v)
                    arr = cls.to_json_string(arr)
                elif list_objs is None:
                    arr = cls.to_json_string([])
                f.write(arr)
                f.close()
