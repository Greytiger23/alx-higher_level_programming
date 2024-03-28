#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
curl -sI -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -sI "$1"
