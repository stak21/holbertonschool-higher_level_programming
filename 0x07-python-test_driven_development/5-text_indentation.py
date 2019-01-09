#!/usr/bin/python3
""" text_indentation: prints newlines after certain characters """


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    buffer = []
    start = 1
    for count in range(len(text)):
        if start and text[count] is " ":
            continue
        start = 0
        print(text[count], end="")
        if text[count] in ".?:":
            print("\n")
            start = 1
