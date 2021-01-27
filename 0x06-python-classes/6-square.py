#!/usr/bin/python3
"""Square"""


class Square:
    """constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, x):
        """setter"""
        if (type(x) is not tuple or len(x) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(x[0]) is not int or type (x[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (x[0]) < 0 or (x[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = x

    def area(self):
        """area square"""
        return self.__size ** 2 

    def my_print(self):
        """print # for each size value
        or " " if [0] is > than 0"""
        if self.__size == 0:
            print()
            return
        if (self.__position[0]) > 0 or self.__size is not 0:
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
