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
        initialize a new base geometry object
        """
        pass

    def area(self):
        """
        public instance that raises an exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates wether a name value is valid
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
