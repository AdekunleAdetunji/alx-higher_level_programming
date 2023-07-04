#!/usr/bin/python31
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "Best school, " * (magic_string.n - 1) + "Best school"
