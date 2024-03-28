#!/bin/bash
# Bash script that takes in a URL and displays all
curl -sX OPTIONS "$1" | grep -i Allow | cut -d ':' -f 2
