#!/usr/bin/python3
"""takes url and sends request"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    a = requests.get(url, auth=(username, password))
    if a.status_code == 200:
        user_info = a.json()
        print(user_info['id'])
    else:
        print("None")
