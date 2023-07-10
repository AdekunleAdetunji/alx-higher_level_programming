#!/usr/bin/python3
"""
This module contains a BaseGeometry class that serves as a parent class to
a Rectangle class
"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """
    A square class that inherits from the Rectangle class above

    args
    @Rectangle: The parent class
    """

    def __init__(self, size):
        """
        Initialize a new square object based on the rectangle class defined
        above
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
