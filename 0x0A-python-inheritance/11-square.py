#!/usr/bin/python3
"""
This module contains a BaseGeometry class that serves as a parent class to
a Rectangle class
"""

Rectangle = __import__("10-square").Rectangle


class Square(Rectangle):
    """
    A square class that inherits from the Rectangle class above

    args
    @Rectangle: The parent class
    """

    def __init__(self, size):
        """
        Initializes a square object that inherits the properties of the
        rectangle class

        args
        @size: The size of the square
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
