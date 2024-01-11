#!/usr/bin/python3
"""module that defines the class"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """represents the class"""
    def __init__(self, size):
        """public instance method"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

