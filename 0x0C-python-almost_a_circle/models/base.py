#!/usr/bin/python3
"""a module which containes Base class"""

import os
import json


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
            list_objs (list): List of objects

        Creates or overwrites file named ClassName.json` with the JSON data.
        If `list_objs` is None, writes an empty list (`[]`).
        """
        from models.square import Square

        if issubclass(cls, Base):
            name = '{}.json'.format(cls.__name__)
            with open(name, 'w', encoding='utf-8') as f:
                if list_objs is not None:
                    arr = []
                    for i in list_objs:
                        d_v = i.to_dictionary()
                        arr.append(d_v)
                    arr = cls.to_json_string(arr)
                else:
                    arr = cls.to_json_string([])
                f.write(arr)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        rst = json.loads(json_string)
        return rst

    @classmethod
    def create(cls, **dictionary):
        """ the class method def create(cls, **dictionary): that returns an
        instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dum = cls(1, 1)
        elif cls.__name__ == 'Square':
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """class method def load_from_file(cls): that returns a list of instances"""
        cls_name = '{}.json'.format(cls.__name__)
        if not os.path.exists(cls_name):
            return []
        with open(cls_name, 'r', encoding='utf-8') as f:
            js_str = f.read()
            py_str = cls.from_json_string(js_str)
            ls_i = []
            for i in py_str:
                ls_i.append(cls.create(**i))
        return ls_i
