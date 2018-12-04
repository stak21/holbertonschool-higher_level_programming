#!/usr/bin/python3
for i in range(65, 91):
    char = chr(i).lower()
    if char != 'q' or char != 'e':
        print(char, end='')
