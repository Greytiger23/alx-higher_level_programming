#!/usr/bin/python3
""""modules the defines the list"""


class Student:
    """defines the class"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method"""
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            if not isinstance(attrs, list) or not all(isinstance(
            attr, str) for attr in attrs):
                raise TypeError("attrs must be a list of string")
        json_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                json_dict[key] = value
        return json_dict

    def reload_from_json(self, json_data):
        """public method"""
        for key, value in json_data.items():
            setattr(self, key, value)
