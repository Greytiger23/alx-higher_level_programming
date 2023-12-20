#!/usr/bin/python3
"""module that defines a square class"""


class Square:
    """represents the class"""
    def __init__(self, size=0):
        """private attribute instalation"""
        if not isinstance(size, int):
            """instalation with option"""
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """public instance method"""
        return self.__size ** 2
