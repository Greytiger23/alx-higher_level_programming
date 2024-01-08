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

class Rectangle(BaseGeometry):
    """represents the class"""
    def __init__(self, width, height):
        """instatiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """public instance method"""
        return self.__width * self.__height

    def __str__(self):
        """public instance method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """represents the class"""
    def __init__(self, size):
        """public instance method"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """public instance method"""
        return self.__size ** 2

    def __str__(self):
        """public instance method"""
        return "[Square] {}/{}".format(self.__size, self.__size)

