#!/usr/bin/python3
"""defines the object class"""


def inherits_from(obj, a_class):
    """defines the class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
