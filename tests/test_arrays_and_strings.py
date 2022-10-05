"""
Tests for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions' in 'Cracking the Coding Interview'.
"""

from cracking_the_coding_interview.arrays_and_strings import (
    are_all_chars_unique)


def test_are_all_chars_unique_valid_correct_outputs():
    assert are_all_chars_unique(string='hello') == False
    assert are_all_chars_unique(string='helo') == True
    assert are_all_chars_unique(string='hel o') == True
    assert are_all_chars_unique(string='hel  o') == False
