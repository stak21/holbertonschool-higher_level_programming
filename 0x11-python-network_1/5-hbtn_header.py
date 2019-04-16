#!/usr/bin/python3
"""
Script: given a URL, send a request display a header
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
