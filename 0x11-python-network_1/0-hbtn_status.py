#!/usr/bin/python3
""" python script that fetches url"""
import urllib.request
from urllib.request import urlopen


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    b = response.read()
    print("Body response:")
    print("\t- type:", type(b))
    print("\t- content:", b)
    print("\t- utf-8 content:", b.decode('utf-8'))
