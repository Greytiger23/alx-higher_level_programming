#!/usr/bin/python3
"""module that defines a square class"""


class Square:
    """represents the class"""
    def __init__(self, size=0, position=(0, 0)):
        """private instance instalation"""
        self.size = size
        self.position = position

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

    def position(self):
        """private instance attribute"""
        return self.position

    def position(self, value):
        """property setter"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(a, int) and a >= 0 for a in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

    def area(self):
        """public instance method"""
        return self.size ** 2

    def my_print(self):
        """public instance method"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
