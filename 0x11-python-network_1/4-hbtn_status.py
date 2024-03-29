#!/usr/bin/python3
"""takes url and sends request"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
if response.status_code == 200:
    d = response.json()
    print("\t- type:", type(d))
    print("\t- content:", d)
else:
    print("Error fetching URL. Status code:", response.status_code)
