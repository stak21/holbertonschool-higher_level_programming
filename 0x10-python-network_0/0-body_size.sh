#!/usr/bin/env bash
# Bash script to send a request to the url and display the body size of the
# response

curl -sI "$1" | awk '/Content-Length/ { print $2 }'
