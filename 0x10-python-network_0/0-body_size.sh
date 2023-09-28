#!/bin/bash
# a Bash script that sends a request to a URL, and displays the size of the body
curl -s -o /dev/null -w "%{size_download}" "$1"
