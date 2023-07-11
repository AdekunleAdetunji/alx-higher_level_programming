#!/usr/bin/python3
"""
This module contains functions that demonstrate how to read and write to
a JSON file
"""


import os
import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if not os.path.isfile("add_item.json"):
    save_to_json_file([], "add_item.json")

jsonObj = load_from_json_file("add_item.json")
if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        jsonObj.append(i)
save_to_json_file(jsonObj, "add_item.json")
