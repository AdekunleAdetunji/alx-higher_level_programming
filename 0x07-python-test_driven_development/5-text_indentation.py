#!/usr/bin/python3
"""
This module contains the text_indentation function
Usage:
>>> text_indentation('a.b')
a

b
"""


def text_indentation(text):
    """
    This function adds two new line characters after each occurrences of the
    characters '.:?'

    Args
    @text: The text which that is to be formatted
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    line = []
    for i in text:
        line.append(i)
        if i in ['.', ':', '?']:
            line.append('\n')
            line_str = ''.join(line).strip(" ")
            print(line_str)
            line = []
