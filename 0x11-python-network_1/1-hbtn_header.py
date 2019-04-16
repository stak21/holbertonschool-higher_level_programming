#!/usr/bin/python3
"""Script: takes in a URL and sends a request and display the header
X-Request_ID
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
