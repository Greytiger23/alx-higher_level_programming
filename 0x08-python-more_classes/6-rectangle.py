#!/usr/bin/python3
"""module that defines the class"""


class Rectangle:
    """represents the class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instantiation with option"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def width(self):
        """propety"""
        return self.width

    def width(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    def height(self):
        """property"""
        return self.height

    def height(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

    def area(self):
        """public instance method"""
        return self.width * self.height

    def perimeter(self):
        """public instance method"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """public instance method"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            a = ""
            for b in range(self.height):
                a += "#" * self.width + "\n"
            return a.rstrip()

    def __rep__(self):
        """public instance method"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """public instance method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
