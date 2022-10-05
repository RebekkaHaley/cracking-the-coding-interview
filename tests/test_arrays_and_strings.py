"""
Tests for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

from cracking_the_coding_interview.arrays_and_strings import (
    are_all_chars_unique)


def test_are_all_chars_unique_valid_correct_outputs():
    assert are_all_chars_unique(string='hello') is False
    assert are_all_chars_unique(string='helo') is True
    assert are_all_chars_unique(string='hel o') is True
    assert are_all_chars_unique(string='hel  o') is False
