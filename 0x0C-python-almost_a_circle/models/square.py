#!/usr/bin/python3
"""
This module contains a BaseGeometry class that serves as a parent class to
a Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class that inherits from the Rectangle class above

    args
    @Rectangle: The parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object that inherits the properties of the
        rectangle class

        args
        @size: The size of the square
        @x: The x coordinate of the square
        @y: The y coordinate of the square
        @id: The id of the square
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """
        The getter got the square private instance attribute
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        The setter method for the square private instance attribute
        """
        self.error("dim", "width", size)
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        This method assigns a new value to the instance attributes

        args
           *: variable len arguments
           **: variable len kword argumets
        """
        if args:
            vars = ["id", "size", "x", "y"]
            for idx, val in enumerate(args):
                if idx == 1:
                    setattr(self, "height", val)
                    setattr(self, "width", val)
                else:
                    setattr(self, vars[idx], val)
        elif kwargs:
            for key, val in kwargs.items():
                if key == "size":
                    setattr(self, "height", val)
                    setattr(self, "width", val)
                else:
                    setattr(self, key, val)

    def __str__(self):
        """
        print a human readable representation of the square object
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def to_dictionary(self):
        """
        Returns a dictionary representation of class
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
