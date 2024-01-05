#!/usr/bin/python3
"""module that defines the class"""


class Rectangle:
    """represents the class"""

    def __init__(self, width=0, height=0):
        """instantiation with option"""
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    def width(self):
        """propety"""
        return self._width

    def width(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def height(self):
        """property"""
        return self._height

    def height(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
