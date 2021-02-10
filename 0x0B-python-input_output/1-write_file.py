#!/usr/bin/python3
"""number of lines"""

def write_file(filename="", text=""):
    """reading from file"""
    with open(filename, encoding="utf-8") as x:
        return len(x.readlines())
