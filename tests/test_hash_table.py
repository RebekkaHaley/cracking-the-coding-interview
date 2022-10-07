"""
Tests for Hash Table data structure coded from scratch. TODO: Code is still a WIP.

Resources:
- [Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/)
"""

import pytest

from cracking_the_coding_interview.hash_table import HashTable


@pytest.fixture
def hash_table():
    sample_table = HashTable(capacity=100)
    sample_table["hello"] = "world"
    sample_table[98.6] = 37
    sample_table[False] = True
    return sample_table


def test_should_create_hashtable():
    hash_table = HashTable(capacity=100)
    assert hash_table is not None


def test_should_not_contain_none_value_when_created():
    hash_table = HashTable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values


def test_should_report_capacity():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    actual_value = len(hash_table)
    assert actual_value == expected_value


def test_should_populate_table_with_blank_obj():
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)
    actual_values = hash_table.pairs
    assert actual_values == expected_values


def test_should_insert_key_value_pairs(hash_table):
    assert ("hello", "world" )in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs
    assert len(hash_table) == 100


def test_should_not_grow_when_adding_elements():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    hash_table["hello"] = "world"
    actual_value = len(hash_table)
    assert actual_value == expected_value


def test_should_not_shrink_when_removing_elements():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    hash_table["hello"] = "world"
    del hash_table["hello"]
    actual_value = len(hash_table)
    assert actual_value == expected_value


def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert None in hash_table.pairs


def test_should_find_value_by_key(hash_table):
    assert hash_table["hello"] == "world"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True


def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"


def test_should_find_key(hash_table):
    assert "hello" in hash_table


def test_should_not_find_key(hash_table):
    assert "missing_key" not in hash_table


def test_should_get_value(hash_table):
    assert hash_table.get("hello") == "world"


def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None


def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"


def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hello", "default") == "world"


def test_should_delete_key_value_pair(hash_table):
    assert "hello" in hash_table
    assert ("hello", "world") in hash_table.pairs
    assert len(hash_table) == 100
    del hash_table["hello"]
    assert "hello" not in hash_table
    assert ("hello", "world") not in hash_table.pairs
    assert len(hash_table) == 100


def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"


def test_should_update_value(hash_table):
    assert hash_table["hello"] == "world"
    hash_table["hello"] = "hola"
    assert hash_table["hello"] == "hola"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100


def test_should_return_pairs(hash_table):
    assert ("hello", "world") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs
