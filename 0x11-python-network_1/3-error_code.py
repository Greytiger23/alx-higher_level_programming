#!/usr/bin/python3
# takes url and sends request and displays
import urllib.request
import sys
import urllib.error


url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        b = response.read().decode('utf-8')
        print(b)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
