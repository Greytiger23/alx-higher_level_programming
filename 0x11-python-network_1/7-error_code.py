#!/usr/bin/python3
"""takes url, sends request and displays"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    a = requests.get(url)
    if a.status_code >= 400:
        print("Error code:", a.status_code)
    else:
        print(a.text)
