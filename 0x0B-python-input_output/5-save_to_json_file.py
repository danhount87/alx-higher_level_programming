#!/usr/bin/python3
"""A JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
sh: 1: q: not found
    with open(filename, "w") as f:
        json.dump(my_obj, f)
