#!/usr/bin/python3
"""
Given a string, send a serach request
"""
import requests
import sys

if __name__ == "__main__":
    r =\
    requests.get("https://swapi.co/api/people/?search={}".format(sys.argv[1]))
    dic = r.json()
    print("Number of results: {}".format(dic['count']))
    for res in dic['results']:
        print("{}".format(res['name']))
