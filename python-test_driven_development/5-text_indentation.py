#!/usr/bin/python3
"""
This module provides a function that prints a text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: The input text (must be a string)
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = '.?:'
    buffer = ""
    for char in text:
        buffer += char
        if char in special_chars:
            print(buffer.strip())
            print()
            buffer = ""
    if buffer:
        print(buffer.strip(), end="")
