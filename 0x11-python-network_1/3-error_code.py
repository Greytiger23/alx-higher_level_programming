#!/usr/bin/python3
"""takes url and sends request and displays"""
from urllib.request import urlopen
import sys
from urllib.error import HTTPError
import urllib.request


url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        b = response.read().decode('utf-8')
        print(b)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
