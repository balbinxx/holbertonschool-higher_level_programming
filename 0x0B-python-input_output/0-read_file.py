#!/usr/bin/python3
"""module for read file"""


def read_file(filename=""):
    """Read and print a text file"""
    with open(filename, encoding='utf-8') as x:
        print(x.read(), end="")
