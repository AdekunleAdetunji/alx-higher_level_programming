#!/usr/bin/python3
"""
This module contains a user-defined function that loads JSON object from
a file and converts it to a valid python object data structure
"""


import json


def load_from_json_file(filename):
    """
    Loads aa json file and converts the its content to a valid python data
    structure

    args
       @filename: The file to be read from

    Return
       The python representation of the json text
    """
    with open(filename) as fileObj:
        return json.load(fileObj)
