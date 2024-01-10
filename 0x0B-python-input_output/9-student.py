#!/usr/bin/python3
""""modules the defines the list"""


class Student:
    """defines the class"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """public method"""
        json_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                json_dict[key] = value
        return json_dict
