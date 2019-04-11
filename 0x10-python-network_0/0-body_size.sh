#!/usr/bin/env bash
# Bash script to send a request to the url and display the body size of the
# response

curl -sI 172.31.54.208:42887 | awk '/Content-Length/ { print $2 }'
