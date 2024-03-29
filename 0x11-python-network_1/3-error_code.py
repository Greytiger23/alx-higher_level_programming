#!/usr/bin/python3
"""takes url and sends request and displays"""

from urllib.request import urlopen, Request
import sys
from urllib.error import HTTPError
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    a = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(a) as response:
            b = response.read().decode('utf-8')
            print(b)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
