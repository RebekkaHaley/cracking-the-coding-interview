"""
Tests for StringBuilder data structure coded from scratch.
"""

import pytest

from cracking_the_coding_interview.string_builder import StringBuilder


def test_should_create_empty_string_builder():
    expected_value = ""
    string_builder = StringBuilder()
    assert str(string_builder) == expected_value


def test_should_not_create_stringbuilder_with_args():
    with pytest.raises(TypeError):
        StringBuilder("Hello ")


def test_should_add_strings():
    expected_value = "Hello World"
    string_builder = StringBuilder()
    string_builder.add("Hello ")
    string_builder.add("World")
    assert str(string_builder) == expected_value
