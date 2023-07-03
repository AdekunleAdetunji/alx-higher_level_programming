#!/usr/bin/python3
"""
This module contains a Rectangle class that creates an empty rectangle object
and also an err_check function to check for that the right functions are passed
when creating an instance of the class
"""
def err_check(param, side):
    """This function checks for error in the parameter passed to class"""
    if not isinstance(param, int):
        raise TypeError(f"{side} must be an integer")
    if param < 0:
        raise ValueError(f"{side} must be >= 0")

class Rectangle():
    """
    This  class defines a rectangle
    """

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """This function instantiates the rectangle class"""
        err_check(width, "width")
        err_check(height, "height")
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter of the width instance attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter of the width instance attribute"""
        err_check(width, "width")
        self.__width = width

    @property
    def height(self):
        """Getter of the height instance attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter of the height instance attribute"""
        err_check(height, "height")
        self.__height = height

    def area(self):
        """This method calculates the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """This method calculate and returns perimeter of the rectangle"""
        if not (self.__height and self.__width):
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """This method returns a printable representation of the rectangle"""
        return "\n".join(["#"*self.__width for i in range(self.__height)])

    def __repr__(self):
        """This method return an official representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message to stdout when a rectangle object is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
