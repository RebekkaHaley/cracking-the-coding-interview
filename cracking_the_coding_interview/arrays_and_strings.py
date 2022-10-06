"""
Functions for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

import math


def is_string_chars_unique(string: str) -> bool:
    """Calculates whether all chars in a given string appear only once.

    Args:
        string: Any string.

    Returns:
        True if all characters are unique. Else False.
    """
    counter = {}
    for char in string:
        if char in counter.keys():
            counter[char] += 1
        else:
            counter[char] = 1
    return math.prod(counter.values()) <= 1
