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
        new_data = []
        with open(csv_file) as file:
            for i in csv.DictReader(file):
                new_data.append(i)
        with open("data.json", "w") as file:
            json.dump(new_data, file)
        return True
    except (FileNotFoundError, TypeError):
        return False
