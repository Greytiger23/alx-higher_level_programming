#!/bin/bash
# Bash script that takes in a URL, sends a POST request
# to the passed URL, and displays the body of the response

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
email="test@gmail.com"
subject="I will always be here for PLD"
a=$(curl -sS -d "email=$email&subject=$subject" "$1")
echo "$a"
