#!/usr/bin/python3
"""module that defines the class"""


class Rectangle:
    """represents the class"""
    x = 0
    y = "#"

    def __init__(self, width=0, height=0):
        """instantiation with option"""
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height
        Rectangle.x += 1

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

    def area(self):
        """public instance method"""
        return self._width * self._height

    def perimeter(self):
        """public instance method"""
        return 2 * (self._width + self._height)

    def __str__(self):
        """public instance method"""
        if self._width == 0 or self._height == 0:
            return ""
        else:
            a = ""
            for b in range(self._height):
                a += str(self.y) * self._width + "\n"
            return a.rstrip()

    def __rep__(self):
        """public instance method"""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """public instance method"""
        print("Bye rectangle...")
        Rectangle.x -= 1

    def bigger_or_equal(rect_1, rect_2):
        """static method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a_1 = rect_1.area()
        a_2 = rect_2.area()
        if a_1 >= a_2:
            return rect_1
        else:
            return rect_2
