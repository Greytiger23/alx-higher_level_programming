#!/bin/bash
# Bash script that takes in a URL, sends a POST request
curl -sI -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
