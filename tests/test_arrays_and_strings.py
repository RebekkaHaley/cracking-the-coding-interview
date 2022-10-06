"""
Tests for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

from cracking_the_coding_interview.arrays_and_strings import (
    is_string_chars_unique)


def test_are_all_chars_unique_valid_correct_outputs():
    assert is_string_chars_unique(string='hello') is False
    assert is_string_chars_unique(string='helo') is True
    assert is_string_chars_unique(string='hel o') is True
    assert is_string_chars_unique(string='hel  o') is False
