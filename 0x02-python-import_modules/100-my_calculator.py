#!/usr/bin/python3
import sys
from calculator_1 import add, div, mul, sub

argv = sys.argv
argc = len(argv) - 1
if __name__ == "__main__":
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    if argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
