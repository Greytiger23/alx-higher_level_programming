#!/usr/bin/python3
"""module that defines the class"""


class Rectangle:
    """represents the class"""
    number_of_instances = 0
    print_symbol = "#"

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
                a += str(self.print_symbol) * self.width + "\n"
            return a.rstrip()

    def __rep__(self):
        """public instance method"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """public instance method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
