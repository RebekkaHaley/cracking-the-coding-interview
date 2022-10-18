"""
Tests for StringBuilder data structure coded from scratch.
"""

import pytest
from io import StringIO

from cracking_the_coding_interview.string_builder import StringBuilder, StringBuilderIO


def test_should_create_empty_string_builder():
    expected_value = ""
    string_builder = StringBuilder()
    assert str(string_builder) == expected_value


def test_should_create_empty_string_builder_io():
    string_builder = StringBuilderIO()
    assert isinstance(string_builder.memory, StringIO)


def test_should_not_create_string_builder_with_args():
    with pytest.raises(TypeError):
        StringBuilder("Hello ")


def test_should_not_create_string_builder_io_with_args():
    with pytest.raises(TypeError):
        StringBuilderIO("Hello ")


def test_should_add_strings_to_string_builder():
    expected_value = "Hello World"
    string_builder = StringBuilder()
    string_builder.add("Hello ")
    string_builder.add("World")
    assert str(string_builder) == expected_value


def test_should_add_strings_to_string_builder_io():
    expected_value = "Hello World"
    string_builder = StringBuilderIO()
    string_builder.add("Hello ")
    string_builder.add("World")
    assert str(string_builder) == expected_value
