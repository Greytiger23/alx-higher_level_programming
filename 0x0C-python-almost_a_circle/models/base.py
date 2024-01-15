#!/usr/bin/python3
"""module that defines the base class"""
import json


class Base:
    """represents the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """static method"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """class method"""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        a = "{}.json".format(class_name)
        with open(a, 'w') as file:
            x = [obj.to_dictionary() for obj in list_objs]
            y = cls.to_json_string(x)
            file.write(y)

    def from_json_string(json_string):
        """stactic method"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """class method"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise TypeError("Cannot create an instance for {}".format(cls.__name__))
        dummy_instance.update(**dictionary)
        return dummy_instance

    def load_from_file(cls):
        """class method"""
        b = "{}.json".format(cls.__name__)
        try:
            with open(b, 'r') as file:
                y = file.read()
                x = cls.from_json_string(y)
                return [cls.create(**d) for d in x]
        except FileNotFoundError:
            return []
