#!/usr/bin/python3
"""Square"""


class Square:
    """constructor"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """"area return"""
        return self.__size ** 2

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, aux):
        """setter"""
        if (type(aux) is not int):
            raise TypeError("size must be an integer")
        if (aux < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = aux
