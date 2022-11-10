"""
Tests for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

from ctci.arrays_and_strings import is_unique


def test_should_detect_string_with_unique_chars():
    assert is_unique(string='hello') is False
    assert is_unique(string='helo') is True
    assert is_unique(string='hel o') is True
    assert is_unique(string='hel  o') is False
