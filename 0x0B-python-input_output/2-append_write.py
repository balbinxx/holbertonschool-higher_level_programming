#!/usr/bin/python3
"""writing into a file"""


def write_file(filename="", text=""):
    """writing into a file"""
    with open(filename, mode="a", encoding="utf-8") as x:
        return x.write(text)
