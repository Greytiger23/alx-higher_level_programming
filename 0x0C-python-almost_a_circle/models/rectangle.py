#!/usr/bin/python3
"""module that defines the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """represents the class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def width(self):
        """property"""
        return self.__width

    def width(self, value):
        """property stter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def height(self):
        """property"""
        return self.__height

    def height(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def x(self):
        """property"""
        return self.__x

    def x(self, value):
        """property"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def y(self):
        """property"""
        return self.__y

    def y(self, value):
        """property"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method"""
        return self.width * self.height

    def display(self):
        """public method"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """overriide method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """public method"""
        if args:
            a = ["id", "width", "height", "x", "y"]
            for b, c in enumerate(args):
                setattr(self, a[b], c)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """public method"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
