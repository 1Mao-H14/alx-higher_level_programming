#!/usr/bin/python3

"""a module which containes Base class"""
from models import square

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

    @classmethode
    def save_to_file(cls, list_objs):
        """ class method def save_to_file(cls, list_objs): 
            that writes the JSON string representation of list_objs to a file"""
        if issubclass(cls, Base):
            with open('{}.json'.formate(str(cls)), 'a', encoding=utf-8) as f:
                arr = []
                for i in list_objs:
                    d_v = i.to_dictionary()
                    js_v = d_v.to_json_string()
                    arr.append(js_v)
                f.write(arr)
