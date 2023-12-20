#!/usr/bin/python3
"""module that defines a square class"""


class Square:
    """represents the class"""
    def __init__(self, size=0):
        """private instance attribute"""
        self.size = size

    def size(self):
        """property"""
        return self.size

    def size(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value

    def area(self):
        """public instance method"""
        return int(self.size) * int(self.size)
