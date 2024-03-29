#!/usr/bin/python3
""" python script that fetches url"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    b = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(b)))
    print("\t- content: {}".format(b))
    print("\t- utf-8 content: {}".format(b))
