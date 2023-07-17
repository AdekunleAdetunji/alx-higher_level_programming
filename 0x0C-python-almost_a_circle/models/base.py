#!/usr/bin/python3
"""
This module contains the BaseGeometry class
"""

import csv
import json
import os
import turtle


class Base():
    """This is a base class

    args
    Nill
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize a new base geometry object

        args
           @id: The id of the new object
        """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method to convert a valid list of dictionary representation
        of objects to their JSON representation

        args
           @list_dictionaries: A list of dictionaries
        """
        if not list_dictionaries:
            return "[]"
        elif type(list_dictionaries) == list and \
                all(type(i) == dict for i in list_dictionaries):
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a json representation of list of objects to a file

        args
           @list_objs: a list of objects whose json representation is to
              a file
        """
        with open(cls.__name__ + ".json", 'w') as fileObj:
            list_of_dict = [obj.to_dictionary() for obj in list_objs]
            if not list_objs:
                fileObj.write("[]")
            else:
                fileObj.write(cls.to_json_string(list_of_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        a method that return a valid python data structure from a JSON string

        args
           @json_string: The json string to be converted to valid python DS
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new instance with all instance attributes set

        args
           @dictionary: A dictionary of all the new instance attributes
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
            instance.update(**dictionary)
            return instance
        elif cls.__name__ == "Square":
            instance = cls(1)
            instance.update(**dictionary)
            return instance
        else:
            return cls()

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of json dictionary representation of various objects
        in a file and cretesa and instance for all of this objects

        args
        """
        inst_list = []
        file_name = cls.__name__ + ".json"
        if os.path.exists(file_name):
            with open(file_name) as fileObj:
                json_rep = fileObj.read()
                py_rep = cls.from_json_string(json_rep)
                for dic in py_rep:
                    instance = cls.create(**dic)
                    inst_list.append(instance)
        return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write a csv representation of a list of objects to a csv file

        args
           @list_objs: The list of objects to be written to the csv file
        """
        classname = cls.__name__
        filename = classname + ".csv"
        with open(filename, 'w') as fileObj:
            objDict = [obj.to_dictionary() for obj in list_objs]
            if classname == "Rectangle":
                csvObj = csv.DictWriter(fileObj,
                                        ["id", "width", "height", "x", "y"])
            elif classname == "Square":
                csvObj = csv.DictWriter(fileObj,
                                        ["id", "size", "x", "y"])
            csvObj.writeheader()
            for line in objDict:
                csvObj.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of object represenations in a csv file and create an
        instance of this representations

        args
        """
        filename = cls.__name__ + ".csv"
        inst_list = []
        if os.path.exists(filename):
            with open(filename) as fileObj:
                csvObj = csv.DictReader(fileObj)
                for line in csvObj:
                    dic = {k: int(v) for k, v in line.items()}
                    inst_list.append(cls.create(**dic))
        return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        This method opens and draw a rectangle object and square object

        args
           @list_rectangles: list of rectangles
           @list_squares: list of squares
        """
        t = turtle.Turtle()
        t.penup()
        for obj in list_rectangles + list_squares:
            t.goto(obj.x, obj.y)
            t.pendown()
            for dim in (obj.width, obj.height, obj.width, obj.height):
                t.forward(dim)
                t.right(90)
            t.penup()
