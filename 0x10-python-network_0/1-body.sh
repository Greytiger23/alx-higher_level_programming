#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
a=$(curl -sS -w "%{http_code}" -o response_body.tmp "$1")
s=$(tail -n1 < "$a")
if [ "$s" -eq 200 ]; then
	cat response_body.tmp
else
	echo "Request failed: $s"
fi
rm -f response_body.tmp
