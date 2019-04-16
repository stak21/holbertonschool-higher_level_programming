#!/usr/bin/python3
"""
Script: given a letter, send a POST request
"""
import requests
import sys


if __name__ == "__main__":
    params = {'q': ""}
    if sys.argv[1]:
        params['q'] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', params)
    try:
        if not r.json():
            print("No result")
        else:
            print("[{}] {}hi".format(r.json()['id'], r.json()['name']))
    except:
        print("Not a valid JSON")
