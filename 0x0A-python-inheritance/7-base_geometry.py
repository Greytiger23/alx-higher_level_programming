#!/usr/bin/python3
"""module that defines the class"""


class BaseGeometry:
    """represents the class"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method"""
        if not isinstance(value, int):
            raise TypeError("f{name} must be an integer")
        if value <= 0:
            raise ValueError("f{name} must be greater than 0")
