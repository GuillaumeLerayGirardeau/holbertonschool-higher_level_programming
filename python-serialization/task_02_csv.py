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
    try:
        with open("data.json", "w") as file:
            with open(csv_file) as open_csv:
                json.dump(csv.DictReader(open_csv), file)
                return True
    except (FileNotFoundError, TypeError):
        return False
