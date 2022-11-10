"""
Functions for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

import math


def is_unique(string: str) -> bool:
    """Checks whether all chars in a given string appear only once.

    Args:
        string: Any string.

    Returns:
        True if all characters are unique. Else False.
    """
    memory = ''
    for char in string:
        if char in memory:
            return False
        memory = f'{memory}{char}'
    return True
