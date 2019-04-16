#!/usr/bin/python3
"""
Given a string, send a serach request 
"""
import requests
import sys


r = requests.get("https://swapi.co/api/people/?search={}", sys.argv[1])
