#!/usr/bin/bash
# Bash script to send a request to the url and display the body size of the
curl -w "%{size_download}"\\n -o /dev/null -s $1
