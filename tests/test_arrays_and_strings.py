"""
Tests for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

from ctci.arrays_and_strings import is_unique, check_permutation, urlify


def test_should_correctly_check_if_string_has_unique_chars():
    assert is_unique(string='hello') is False
    assert is_unique(string='helo') is True
    assert is_unique(string='hel o') is True
    assert is_unique(string='hel  o') is False


def test_should_correctly_check_if_two_strings_are_permutations():
    assert check_permutation(string='listen', target='silent') is True
    assert check_permutation(string='foo', target='bar') is False


def test_should_convert_string_to_url():
    assert urlify(string='Mr John Smith', true_len=13) == 'Mr%20John%20Smith'


def test_should_handle_trailing_whitespace():
    assert urlify(string='Mr John Smith     ', true_len=13) == 'Mr%20John%20Smith'


def test_should_handle_blank_string():
    assert urlify(string='', true_len=0) == ''
