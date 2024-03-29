#!/usr/bin/python3
"""takes url and sends request"""
import requests
import sys


username = sys.argv[1]
password = sys.argv[2]
url = 'https://api.github.com/user'
a = requests.get(url, auth=(username, password))
if a.status_code == 200:
    user_info = a.json()
    print("Your GitHub user ID is:", user_info['id'])
else:
    print("Failed to retrieve user information. Status code:", a.status_code)
