#!/usr/bin/python3
"""takes url and requests and displays"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    a = urllib.request.Request(url)
    with urllib.request.urlopen(a) as response:
        b = response.headers.get('X-Request-Id')
        print(b)
