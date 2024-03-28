#!/bin/bash
# Bash script that takes in a URL and displays all
curl -sI -X OPTIONS "$1" | grep -i allow | cut -d ':' -f 2
