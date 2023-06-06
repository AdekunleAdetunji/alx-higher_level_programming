#!/usr/bin/python3
def print_last_digit(number):
    if number < 0 and number % 10 != 0:
        print(10 - number % 10, end="")
        return (10 - number % 10)
    else:
        print(number % 10, end="")
        return (number % 10)
