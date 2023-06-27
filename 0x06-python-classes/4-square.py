#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains a new version of the square
class defined in 2-task"""


class Square():
    """This is a richer version of square class in 2-task with
    an additional method"""
    def __init__(self, size=0):
        """
        Initialization of the square class

        Args:
        size: A private instance attribute of the square size
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

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
