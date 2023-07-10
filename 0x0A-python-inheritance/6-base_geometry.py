#!/usr/bin/python3
"""
This module contains an empty class
"""


class BaseGeometry():
    """This is an empty class

    args
    Nill
    """
    def __init__(self):
        """
        initialize a new BaseGeometry object
        """
        pass

    def area(self):
        """
        public instance that raises an exception when called
        """
        raise Exception("area() is not implemented")
