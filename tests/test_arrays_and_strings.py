"""
Tests for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""

from ctci.arrays_and_strings import (is_unique, check_permutation, urlify, one_away)


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


def test_should_not_ignore_multiple_inner_whitespace():
    assert urlify(string='Mr  John Smith', true_len=13) == 'Mr%20%20John%20Smith'


def test_should_return_true_where_edits_are_exactly_one_away():
    assert one_away(before='pale', after='ple') == True
    assert one_away(before='pale', after='pales') == True
    assert one_away(before='pale', after='bale') == True


def test_should_return_false_where_edits_are_greater_than_one_away():
    assert one_away(before='pale', after='pl') == False
    assert one_away(before='pale', after='palesq') == False
    assert one_away(before='pale', after='bake') == False


def test_should_return_true_where_unedited():
    assert one_away(before='pale', after='pale') == True


def test_should_handle_edits_with_duplicate_characters():
    assert one_away(before='pale', after='palee') == True
    assert one_away(before='pale', after='paless') == False


def test_should_handle_edits_with_blank_string():
    assert one_away(before='', after='p') == True
    assert one_away(before='p', after='') == True
    assert one_away(before='', after='') == True
