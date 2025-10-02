#!/usr/bin/python3
"""
Function to serialize and deserialize xml
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize a file to xml
    """
    data = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(data, key)
        child.text = str(value)
    tree = ET.ElementTree(data)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    deserialize a file from xml
    """
    new_dict = {}
    element = ET.parse(filename)
    root = element.getroot()
    for i in root:
        new_dict[i.tag] = i.text
    return new_dict
