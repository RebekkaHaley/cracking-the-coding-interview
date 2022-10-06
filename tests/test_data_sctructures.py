"""
Tests for data structures coded from scratch.
"""

from cracking_the_coding_interview.data_sctructures import (
    HashTable)


def test_hashtable_should_create_valid():
    hash_table = HashTable(capacity=100)
    assert hash_table is not None


def test_hashtable_should_report_capacity():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    actual_value = len(hash_table)
    assert actual_value == expected_value


def test_hashtable_should_populate_with_none():
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)
    actual_values = hash_table.values
    assert actual_values == expected_values
