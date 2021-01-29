#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """define rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height is 0 or self.__width is 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        new_str = ""
        if self.__width is 0 or self.__height is 0:
            return new_str
        else:
            for x in range(self.__height):
                if x + 1 < self.__height:
                    new_str += "#" * self.__width + "\n"
                else:
                    new_str += "#" * self.__width
        return new_str

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
