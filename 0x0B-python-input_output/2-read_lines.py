#!/usr/bin/python3
""" Function: read_lines """


def read_lines(filename="", nb_lines=0):
    """ read n lines of a text file and prints it to the stdout """
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if nb_lines is not 0 and count == nb_lines:
                break
            print(line, end="")
            count += 1


print("1 line:")
read_lines("my_file_0.txt", 1)
print("--")
print("3 lines:")
read_lines("my_file_0.txt", 3)
print("--")
print("Full content:")
read_lines("my_file_0.txt")
