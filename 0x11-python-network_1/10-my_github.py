#!/usr/bin/python3
"""
Send a request to github with a user and password
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if len(sys.argv) == 3:
    params = sys.argv[1]
    r = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(
        sys.argv[1], sys.argv[2]))
    try:
        print(r.json()['id'])
    except:
        print("None")
