#!/usr/bin/python3
"""
Script: given a letter, send a POST request
"""
import requests
import sys


if __name__ == "__main__":
    params = {'q': ""}
    if len(sys.argv) == 2 and sys.argv[1]:
        params['q'] = sys.argv[1]
    if not params['q']:
        print("No result")
    r = requests.post('http://0.0.0.0:5000/search_user', params)
    try:
        if not r.json():
            print("No result")
        else:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except:
        print("Not a valid JSON")
