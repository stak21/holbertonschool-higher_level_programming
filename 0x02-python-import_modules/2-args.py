#!/usr/bin/python3

if __name__ == "__main__":
    import sys

for argv in sys.argv:
    print("{} {}".format(len(argv), argv))
