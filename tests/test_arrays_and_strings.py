"""
Tests for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

from ctci.arrays_and_strings import is_unique, check_permutation


def test_should_correctly_check_if_string_has_unique_chars():
    assert is_unique(string='hello') is False
    assert is_unique(string='helo') is True
    assert is_unique(string='hel o') is True
    assert is_unique(string='hel  o') is False


def test_should_correctly_check_if_two_strings_are_permutations():
    assert check_permutation(string='listen', target='silent') is True
    assert check_permutation(string='foo', target='bar') is False
