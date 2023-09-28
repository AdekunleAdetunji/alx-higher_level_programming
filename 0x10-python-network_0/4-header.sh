#!/bin/bash
# A Bash script that sends a GET request to a URL with header variables sent
curl -sH "X-School-User-Id: 98" "$1"
