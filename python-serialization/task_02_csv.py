#!/usr/bin/python3
"""
Function convert_csv_to_json
"""

import csv
import json


def convert_csv_to_json(csv_file):
    """
    This function convert csv file to json file
    """
    with open("data.json", "w") as file:
        try:
            json.dump(csv.DictReader(csv_file), file)
            return True
        except FileNotFoundError:
            return False
