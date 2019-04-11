#!/bin/bash
# Bash script to send a request to the url and display the body size of the
curl -sI "$1" | awk '/Content-Length/ { print $2 }'
