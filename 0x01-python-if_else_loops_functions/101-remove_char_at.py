#!/usr/bin/python3
def remove_char_at(str, n):
    ls = []
    for ind, char in enumerate(str):
        if ind != n:
            ls.append(char)
    return "".join(ls)
