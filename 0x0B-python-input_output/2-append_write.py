#!/usr/bin/python3
"""defines the module class"""


def append_write(filename="", text=""):
    """represents the write file"""
    with open(filename, "a", encoding="utf-8") as file:
        c = file.write(text)
        return c
