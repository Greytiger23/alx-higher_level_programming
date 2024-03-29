#!/usr/bin/python3
"""takes url, send request and displays"""
import requests
import sys


url = sys.argv[1]
response = requests.get(url)
if 'X-Request-Id' in response.headers:
    x_request_id = response.headers['X-Request-Id']
    print("X-Request-Id:", x_request_id)
else:
    print("X-Request-Id not found in the response headers.")
