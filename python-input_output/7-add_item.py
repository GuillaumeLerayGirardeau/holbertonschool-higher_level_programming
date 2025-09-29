#!/usr/bin/python3

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    file_json = load_from_json_file("add_item.json")
except FileNotFoundError:
    file_json = []

file_json.extend(sys.argv[1:])
save_to_json_file(file_json, "add_item.json")
