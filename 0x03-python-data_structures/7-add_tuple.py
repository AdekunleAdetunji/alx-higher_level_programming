#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    else:
        ls_a = list(tuple_a)
        ls_b = list(tuple_b)
        ls_a.extend([0, 0])
        ls_b.extend([0, 0])
        return (ls_a[0] + ls_b[0]), (ls_a[1] + ls_b[1])
