"""
Tests for Hash Table data structure coded from scratch. TODO: Code is still a WIP.

Resources:
- [Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/)
"""

import pytest
from pytest_unordered import unordered
from unittest.mock import patch

from cracking_the_coding_interview.hash_table import HashTable, Pair


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


def test_should_iterate_over_keys(hash_table):
    for key in hash_table.keys:
        assert key in ("hello", 98.6, False)


def test_should_iterate_over_values(hash_table):
    for value in hash_table.values:
        assert value in ("world", 37, True)


def test_should_iterate_over_pairs(hash_table):
    for key, value in hash_table.pairs:
        assert key in hash_table.keys
        assert value in hash_table.values


def test_should_iterate_over_instance(hash_table):
    for key in hash_table:
        assert key in ("hello", 98.6, False)


def test_should_use_dict_literal_for_str(hash_table):
    assert str(hash_table) in {
        "{'hello': 'world', 98.6: 37, False: True}",
        "{'hello': 'world', False: True, 98.6: 37}",
        "{98.6: 37, 'hello': 'world', False: True}",
        "{98.6: 37, False: True, 'hello': 'world'}",
        "{False: True, 'hello': 'world', 98.6: 37}",
        "{False: True, 98.6: 37, 'hello': 'world'}",
    }


def test_should_have_canonical_string_representation(hash_table):
    assert repr(hash_table) in {
        "HashTable.from_dict({'hello': 'world', 98.6: 37, False: True})",
        "HashTable.from_dict({'hello': 'world', False: True, 98.6: 37})",
        "HashTable.from_dict({98.6: 37, 'hello': 'world', False: True})",
        "HashTable.from_dict({98.6: 37, False: True, 'hello': 'world'})",
        "HashTable.from_dict({False: True, 'hello': 'world', 98.6: 37})",
        "HashTable.from_dict({False: True, 98.6: 37, 'hello': 'world'})",
    }


def test_should_create_hashtable_from_dict():
    dictionary = {"hello": "world", 98.6: 37, False: True}
    hash_table = HashTable.from_dict(dictionary)
    assert hash_table.capacity == len(dictionary) * 10
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.pairs == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())


def test_should_create_hashtable_from_dict_with_custom_capacity():
    dictionary = {"hello": "world", 98.6: 37, False: True}
    hash_table = HashTable.from_dict(dictionary, capacity=100)
    assert hash_table.capacity == 100
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.pairs == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())


def test_should_compare_equal_to_itself(hash_table):
    assert hash_table == hash_table


def test_should_compare_equal_to_copy(hash_table):
    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()


def test_should_compare_equal_different_key_value_order(hash_table):
    h1 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = HashTable.from_dict({"b": 2, "a": 1, "c": 3})
    assert h1 == h2


def test_should_compare_unequal(hash_table):
    other = HashTable.from_dict({"different": "value"})
    assert hash_table != other


def test_should_compare_unequal_another_data_type(hash_table):
    assert hash_table != 42


def test_should_copy_keys_values_pairs_capacity(hash_table):
    copy = hash_table.copy()
    assert copy is not hash_table
    assert set(hash_table.keys) == set(copy.keys)
    assert unordered(hash_table.values) == copy.values
    assert set(hash_table.pairs) == set(copy.pairs)
    assert hash_table.capacity == copy.capacity


def test_should_compare_equal_different_capacity():
    data = {"a": 1, "b": 2, "c": 3}
    h1 = HashTable.from_dict(data, capacity=50)
    h2 = HashTable.from_dict(data, capacity=100)
    assert h1 == h2


def test_should_handle_hash_collisions_with_linear_probing():
    expected_pair_one = Pair(key='first', value='example one')
    expected_pair_two = Pair(key='second', value='example two')
    with patch("builtins.hash", return_value=24):
        hash_table = HashTable(capacity=100)
        hash_table["first"] = "example one"
        hash_table["second"] = "example two"
    assert hash_table._slots[24] == expected_pair_one
    assert hash_table._slots[25] == expected_pair_two
