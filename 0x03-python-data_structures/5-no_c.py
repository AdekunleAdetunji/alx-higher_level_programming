#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    ls = []
    for char in my_string:
        if char != 'c' or char != "C":
            ls.append(char)
    return ("".join(ls))
