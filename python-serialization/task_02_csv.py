#!/usr/bin/python3
"""
Read data from CSV format and converting it into JSON
"""


import json
import csv


def convert_csv_to_json(csv_filename):
    """
    Function that convert CSV format to JSON

    Args:
        csv_filename (str): filename csv format
    """
    try:
        with open(csv_filename, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", mode="w") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except Exception as e:
        print(f"An error occurred: {e}.")
        return False
