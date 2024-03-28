#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as
# the first argument and displays the body of the response

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
a=$(curl -sS -X DELETE -w "%{http_code}" -o response_body.tmp "$1")
b=$(tail -n1 < "$a")
cat response_body.tmp
rm -f response_body.tmp
if ! [[ "$b" =~ ^2 ]]; then
	echo "Request fail: $b"
fi
