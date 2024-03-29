#!/usr/bin/python3
# takes url and requests and displays
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print("X-Request-Id:", x_request_id)
