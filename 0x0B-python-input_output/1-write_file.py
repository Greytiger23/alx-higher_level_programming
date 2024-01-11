#!/usr/bin/python3
"""defines the module class"""


def write_file(filename="", text=""):
    """represents the write file"""
    with open(filename, "w", encoding="utf-8") as file:
        c = file.write(text)
        return c 
