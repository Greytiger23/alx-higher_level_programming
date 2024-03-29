#!/usr/bin/python3
"""takes url and sends request"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    if response.status_code == 200:
        d = response.json()
        print("Body response:")
        print("\t- type:", type(d))
        print("\t- content:", d)
