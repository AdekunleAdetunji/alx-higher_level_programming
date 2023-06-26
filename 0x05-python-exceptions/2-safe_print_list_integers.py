#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        val = 0
        for index in range(x):
            if isinstance(my_list[index], int):
                val += 1
                print("{:d}".format(my_list[index]), end='')
        print("")
        return val
    except Exception as e:
        raise
