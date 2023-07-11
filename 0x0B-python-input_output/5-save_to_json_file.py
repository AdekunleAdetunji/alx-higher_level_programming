#!/usr/bin/python3
"""
This module contains a python function that writes the JSON object
representation of a python data structure to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes a JSON object replica of a python data structure to a
    file

    args
        @my_obj: The python object to be converted to a JSON replica and
        written to the file
        @file_name: The name of the file we are writing to
    """

    with open(filename, 'w', encoding="utf-8") as fileObj:
        json.dump(my_obj, fileObj)
