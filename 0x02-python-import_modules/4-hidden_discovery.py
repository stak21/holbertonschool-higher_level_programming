#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    import sys

for names in dir(hidden_4):
    if names[0] != "_":
        print("{}".format(names))
