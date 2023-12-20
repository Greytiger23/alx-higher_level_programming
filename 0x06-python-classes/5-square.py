#!/usr/bin/python3
"""module that defines a square class"""


class Square:
    """represents the class"""
    def __init__(self, size=0):
        """private instance instalation"""
        self.size = size

    def size(self):
        """property"""
        return self.__size

    def size(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """public instance method"""
        return self.__size ** 2

    def my_print(self):
        """public instance method"""
        if (self.__size == 0):
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
