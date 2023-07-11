#!/usr/bin/python3
"""
This module contains a write_file() function demonstrating how
to write to file objects in python
"""


def append_write(file_name="", text=""):
    """
    This function append a body of text to a file named file_name
    If the file named file_name does exist already it appends the former
    content and if it does not exist then it creates the file

    args
    @file_name: The file_name to be appended to
    @text: The content to be written to the file
    """
    with open(file_name, mode='a', encoding="utf-8") as fileObj:
        return fileObj.write(text)
