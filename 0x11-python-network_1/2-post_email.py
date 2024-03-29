#!/usr/bin/python3
"""takes url and email and posts request"""
from urllib.request import urlopen
from urllib.parse import urlencode
import sys
import urllib.request
import urllib.parse


url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('utf-8')
c = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(c) as response:
    b = response.read().decode('utf-8')
print(b)
