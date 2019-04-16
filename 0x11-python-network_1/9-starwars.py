#!/usr/bin/python3
"""
Given a string, send a serach request
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get("https://swapi.co/api/people/?search={}", sys.argv[1])
