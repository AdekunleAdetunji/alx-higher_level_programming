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

    def to_json(self, attr=None):
        """
        Returns the dictionary representation of the attributes of the class
        instance

        args
           @attr: The attribute whose key:value pair is to be recovered
        """
        attr_dict = self.__dict__
        if type(attr) == list and all(type(i) == str for i in attr):
            return {key: value for key, value in attr_dict.items()
                    if key in attr}
        return self.__dict__

    def reload_from_json(self, json):
        """
        This method rewrites the attributes of an instance using the json file
        supplied to it

        args
           @json: The json dictionary object supplied to the method
        """
        for key, value in json.items():
            setattr(self, key, value)
