#!/usr/bin/python3
"""
This module contains a BaseGeometry class that serves as a parent class to
a Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    This class is a child of BaseGeometry class defined above
    It creates a rectangle instance that has the properties of the BaseGeometry
    when called

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
