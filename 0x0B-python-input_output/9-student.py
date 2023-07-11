#!/usr/bin/python3
"""
This module contains a student class that defines a student
"""


class Student():
    """
    This class defines a student with instantiation with basic attributes of
    a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a new student object

        args
           @first_name: The student first name
           @last_name: The student last name
           @age: The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of the attributes of the class
        instance
        """
        return self.__dict__
