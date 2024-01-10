#!/usr/bin/python3
"""module that defines the json"""


def class_to_json(obj):
    """defines the json"""
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object is not an instance of a class.")
    a = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            a[key] = value
    return a
