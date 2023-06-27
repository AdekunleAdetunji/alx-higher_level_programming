#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains a new version of the square
class defined in 2-task"""


class Square():
    """This is a richer version of square class in 2-task with
    an additional method"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of the square class

        Args:
        size: A private instance attribute of the square size
        position: A private instance attribute of a two integer tuple
        """
        self.__size = size
        self.__position = position
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        elif (not isinstance(self.__position, tuple)
              or len(self.__position) != 2
              or not isinstance(self.__position[0], int)
              or not isinstance(self.__position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Computes and return the area of the square"""
        return (self.__size)**2

    @property
    def size(self):
        """A getter to retrieve the value stored in the private instance
        attrbute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter to set the value stored in the private instace variable"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """A getter to get the position tuple"""
        return self.__position

    @position.setter
    def position(self, tup):
        """A setter function to set the private attribute position"""
        if (not isinstance(tup, tuple) or len(tup) != 2
            or not isinstance(tup[0], int) or not isinstance(tup[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = tup

    def my_print(self):
        """prints to the stdout a square  of size equal to size and filled
        with # characters"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("\n", end="")
