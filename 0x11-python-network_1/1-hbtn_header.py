#!/usr/bin/python3
"""takes url and requests and displays"""
from urllib.request import urlopen
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
