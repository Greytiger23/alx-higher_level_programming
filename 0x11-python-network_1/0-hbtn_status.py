#!/usr/bin/python3
""" python script that fetches url"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    b = response.read()
    print("Body response:")
    print("  - type:",type(b))
    print("  - content:", b.decode('utf-8'))
    print("  - utf-8 content:", b.decode('utf-8'))
