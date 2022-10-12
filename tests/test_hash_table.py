"""
Tests for Hash Table data structure coded from scratch. TODO: Code is still a WIP.

Resources:
- [Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/)
"""

import pytest
from pytest_unordered import unordered

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
    assert None not in hash_table.values


def test_should_report_length(hash_table):
    assert len(hash_table) == 3


def test_should_report_length_of_empty_hash_table():
    hash_table = HashTable(capacity=100)
    assert len(hash_table) == 0


def test_should_create_empty_pair_slots():
    """NB: This tests internal implementation instead of public interfaces, i.e., white-box testing.
    """
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)
    actual_values = hash_table._slots
    assert actual_values == expected_values


def test_should_insert_key_value_pairs(hash_table):
    assert ("hello", "world" )in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs
    assert len(hash_table) == 3


def test_capacity_should_not_grow_when_adding_elements():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    hash_table["hello"] = "world"
    actual_value = len(hash_table._slots)
    assert actual_value == expected_value


def test_capacity_should_not_shrink_when_removing_elements():
    expected_value = 100
    hash_table = HashTable(capacity=expected_value)
    hash_table["hello"] = "world"
    del hash_table["hello"]
    actual_value = len(hash_table._slots)
    assert actual_value == expected_value


def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.pairs


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
    assert len(hash_table) == 3
    del hash_table["hello"]
    assert "hello" not in hash_table
    assert ("hello", "world") not in hash_table.pairs
    assert len(hash_table) == 2


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
    assert len(hash_table) == 3


def test_should_return_pairs(hash_table):
    expected_values = {("hello", "world"), (98.6, 37), (False, True)}
    assert hash_table.pairs == expected_values


def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs


def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs


def test_should_get_pairs_of_empty_hash_table():
    assert HashTable(capacity=100).pairs == set()


def test_should_return_duplicate_values():
    hash_table = HashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    expected_values = [24, 42, 42]
    assert unordered(hash_table.values) == expected_values


def test_should_get_values(hash_table):
    expected_values = ["world", 37, True]
    assert unordered(hash_table.values) == expected_values


def test_should_get_values_of_empty_hash_table():
    assert HashTable(capacity=100).values == []


def test_should_return_copy_of_values(hash_table):
    assert hash_table.values is not hash_table.values


def test_should_get_keys(hash_table):
    assert hash_table.keys == {"hello", 98.6, False}


def test_should_get_keys_of_empty_hash_table():
    assert HashTable(capacity=100).keys == set()


def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys


def test_should_convert_to_dict(hash_table):
    dictionary = dict(hash_table.pairs)
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == unordered(hash_table.values)


def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=0)


def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=-100)


def test_should_not_create_hashtable_with_wrong_type_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity='100')


def test_should_report_capacity(hash_table):
    assert hash_table.capacity == 100


def test_should_report_capacity_of_empty_hash_table():
    assert HashTable(capacity=100).capacity == 100
