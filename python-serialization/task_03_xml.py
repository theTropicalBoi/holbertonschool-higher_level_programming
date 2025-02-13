#!/usr/bin/python3
"""
Serialization and deserialization using XML instead of JSON
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dict to be serialized
        filename (str): The name of the XML file
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file)

def deserialize_from_xml(filename):
    """
    Deserialize and XML file to a python dictionary

    Args:
        filename (str): The XML file
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
