#!/usr/bin/python3
"""bla bla bla"""


def add_integer(a, b=98):
    """Add two integers (a and b)
    a and b should be int or float type
    return int add"""
    if type(a) is int or type(a) is float:
        a = int(a)
    if type(b) is int or type(b) is float:
        b = int(b)
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (a + b)
