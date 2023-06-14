#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev = 0
    total = 0
    for char in roman_string:
        value = dic[char]
        if value > prev:
            total += value - 2 * prev
        else:
            total += value
        prev = value
    return total
