#!/bin/bash
# Bash script that takes in a URL and displays all
# HTTP methods the server will accept

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
a=$(curl -sSI -X OPTIONS "$1")
b=$(echo "$a" | grep -i "Allow")
c=$(echo "$b" | cut -d ' ' -f 2-)
echo "$c"
