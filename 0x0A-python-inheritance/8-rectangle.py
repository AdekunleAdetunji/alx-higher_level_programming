#!/usr/bin/python3
"""
This module contains a BaseGeometry class that serves as a parent class to
a Rectangle class
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


class Rectangle(BaseGeometry):
    """
    This class inherits from the BaseGeometry class defined above

    args
    @BaseGeometry: The parent class
    """

    def __init__(self, width, height):
        """
        Initializes a new rectangle instance when called

        args
        @width: The width of the rectangle instance
        @height: The height of the rectangle instance
        """
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
