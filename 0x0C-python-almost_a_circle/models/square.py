#!/usr/bin/python3
"""module that defines the rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents the class"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def size(self):
        """property"""
        return self.width

    def size(self, value):
        """property setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """overload"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """public method"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for a, b in enumerate(args):
                setattr(self, attrs[a], b)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
