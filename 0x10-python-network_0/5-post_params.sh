#!/bin/bash
# # A Bash script that sends a POST request to a URL with a variables sent
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -X "POST" "$1"
