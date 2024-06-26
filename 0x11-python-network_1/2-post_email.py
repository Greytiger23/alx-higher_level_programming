#!/usr/bin/python3
"""takes url and email and posts request"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    c = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(c) as response:
        b = response.read().decode('utf-8')
    print("Your email is:", email)
    print(b)
