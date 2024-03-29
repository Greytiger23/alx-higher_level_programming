#!/usr/bin/python3
"""takes url and sends request"""
import requests
import sys


if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""
a = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})
try:
    json_data = a.json()
    if json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
