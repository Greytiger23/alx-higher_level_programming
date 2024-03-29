#!/usr/bin/python3
"""takes url, send request and displays"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    a = requests.get(url)
    if 'X-Request-Id' in a.headers:
        x = a.headers['X-Request-Id']
        print(x)
