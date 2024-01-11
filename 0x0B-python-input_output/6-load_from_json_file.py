#!/usr/bin/python3
"""module that defines the list"""
import json


def load_from_json_file(filename):
    """defines the file"""
    with open(filename) as file:
        json_data = json.load(file)
        return json_data
