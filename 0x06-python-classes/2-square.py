#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains an a new version of the square class defined in
1-task
"""


class Square():
    """This class defines a sqaure"""
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
