#!/usr/bin/python3
for i in range(0, 100):
    if i is not 99:
        print("{:0>2d}, ".format(i), end='')
    else:
        print("{}".format(i))
