#!/usr/bin/python3
"""Module for reading a text file"""
import json
import sys
SaveJson = __import__('5-save_to_json_file').save_to_json_file
LoadJson = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"


try:
    args = LoadJson(filename)
except FileNotFoundError:
    args = []

args.extend(sys.argv[1:])

SaveJson(args, filename)
