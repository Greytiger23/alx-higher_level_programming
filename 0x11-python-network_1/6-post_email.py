#!/usr/bin/python3
"""takes url and email, sends request"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    a = requests.post(url, data=data)
    print("Your email is:", a.text)
