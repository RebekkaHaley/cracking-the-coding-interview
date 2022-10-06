"""
Tests for Hash Table data structure coded from scratch.
"""

import pytest

from cracking_the_coding_interview.hash_table import (
    BLANK,
    HashTable)


@pytest.fixture
def hash_table():
    sample_table = HashTable(capacity=100)
    sample_table["hello"] = "world"
    sample_table[98.6] = 37
    sample_table[False] = True
    return sample_table


def test_hashtable_should_create_valid():
    hash_table = HashTable(capacity=100)
    assert hash_table is not None


def test_hashtable_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values


def test_hashtable_should_report_capacity():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    actual_value = len(hash_table)
    assert actual_value == expected_value


def test_hashtable_should_populate_with_blank_obj():
    expected_values = [BLANK, BLANK, BLANK]
    hash_table = HashTable(capacity=3)
    actual_values = hash_table.values
    assert actual_values == expected_values


def test_hashtable_should_insert_key_value_pairs(hash_table):
    assert "world" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values


def test_hashtable_should_not_grow_when_adding_elements():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    hash_table["hello"] = "world"
    actual_value = len(hash_table)
    assert actual_value == expected_value


@pytest.mark.skip
def test_hashtable_should_not_shrink_when_removing_elements():
    hash_table = HashTable(capacity=100)
    pass


def test_hashtable_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert None in hash_table.values


@pytest.mark.skip
def test_hashtable_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
