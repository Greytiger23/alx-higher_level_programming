#!/usr/bin/python3
"""takes url and sends request"""

import requests
import sys

if __name__ == "__main__":
    b = len(sys.agv)
    if b > 1:
        c = sys.argv[1]
    else:
        c = ""
    a = requests.post("http://0.0.0.0:5000/search_user", data={'q': c})
    try:
        j = a.json()
        if j:
            print("[{}] {}".format(j['id'], j['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
