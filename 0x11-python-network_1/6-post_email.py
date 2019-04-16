#!/usr/bin/python3
"""
Script: given a URL and an email, send a POST request
"""
import requests
import sys

if __name__ == "__main__":
    values = { email: sys.argv[2] }
    r = requests.post(sys.argv[1], values)
    print("{}".format(r.text))

