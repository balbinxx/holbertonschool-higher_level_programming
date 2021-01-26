#!/usr/bin/python3
"""Square"""


class Square:
    """validation of size"""
    def __init__(self, size = 0):
        aux = size
        
        if (type(aux) is not int):
            raise TypeError("size must be an integer")
        if (aux < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = aux
