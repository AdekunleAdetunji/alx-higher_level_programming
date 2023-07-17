#!/usr/bin/python3
"""
This module contains a BaseGeometry class that serves as a parent class to
a Rectangle class
"""


from models.base import Base


def error(kind, name, value):
    """
    check for input value and return an error if wrong value or value type is
    supplied
    """
    if type(value) != int:
        raise TypeError(f"{name} must be an integer")
    if kind == "dim":
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
    if kind == "coor":
        if value < 0:
            raise ValueError(f"{name} must be >= 0")


class Rectangle(Base):
    """
    This class inherits from the BaseGeometry class defined above

    args
    @BaseGeometry: The parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new rectangle instance when called

        args
        @width: The width of the rectangle instance
        @height: The height of the rectangle instance
        """
        Base.__init__(self, id)
        self.error = error
        self.error("dim", "width", width)
        self.__width = width
        self.error("dim", "height", height)
        self.__height = height
        self.error("coor", "x", x)
        self.__x = x
        self.error("coor", "y", y)
        self.__y = y

    @property
    def width(self):
        """
        Rectangle width getter method
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter method to set the instance width

        args
           @width: The width of the rectangle
        """
        self.error("dim", "width", width)
        self.__width = width

    @property
    def height(self):
        """
        Rectangle height getter method
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter method to set the instance height

        args
           @height: The height of the rectangle
        """
        self.error("dim", "height", height)
        self.__height = height

    @property
    def x(self):
        """
        Rectangle coordinate x getter method
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter method to set the private instance attribute x

        args
           @x: The x coordinate of the rectangle
        """
        self.error("coor", "x", x)
        self.__x = x

    @property
    def y(self):
        """
        Rectangle coordinate y getter method
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter method to set the private instance attribute y

        args
           @y: The y coordinate of the rectangle
        """
        self.error("coor", "y", y)
        self.__y = y

    def area(self):
        """
        Calculate the area of a rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """display a rectangle filled with # value"""
        for val in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        print a human readable representation of the rectangle object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
        This method assigns a new value to the instance attributes

        args
           *: variable len arguments
           **: variable len kword argumets
        """
        if args:
            vars = ["id", "width", "height", "x", "y"]
            for idx, val in enumerate(args):
                setattr(self, vars[idx], val)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Returns a dictionary representation of class
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
