#!/usr/bin/python3

import csv 
import json

def convert_csv_to_json(csv_file):
    with open("data.json", "w") as file:
        try:
            json.dump(csv.DictReader(csv_file), file)
            return True
        except:
            return False