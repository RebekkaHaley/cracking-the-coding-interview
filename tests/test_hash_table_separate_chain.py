"""
Tests for Hash Table using separate chaining to handle collisions.

Resources:
- [Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/)
"""

import pytest
from pytest_unordered import unordered
from unittest.mock import patch
from collections import deque

from ctci.hash_table_separate_chain import SeparateChainHashTable, Pair


@pytest.fixture
def hash_table():
    sample_table = SeparateChainHashTable(capacity=100)
    sample_table["hello"] = "world"
    sample_table[98.6] = 37
    sample_table[False] = True
    return sample_table


def test_should_create_hashtable():
    hash_table = SeparateChainHashTable(capacity=100)
    assert hash_table is not None


def test_should_not_contain_none_value_when_created():
    hash_table = SeparateChainHashTable(capacity=100)
    assert None not in hash_table.values


def test_should_report_length(hash_table):
    assert len(hash_table) == 3


def test_should_report_length_of_empty_hash_table():
    hash_table = SeparateChainHashTable(capacity=100)
    assert len(hash_table) == 0


def test_should_create_empty_buckets():
    expected_capacity = 3
    expected_values = [deque() for _ in range(expected_capacity)]
    hash_table = SeparateChainHashTable(capacity=expected_capacity)
    actual_values = hash_table._buckets
    assert actual_values == expected_values


def test_should_insert_key_value_pairs(hash_table):
    assert ("hello", "world" )in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs
    assert len(hash_table) == 3


def test_capacity_should_not_grow_when_adding_elements():
    expected_value = 100
    hash_table = SeparateChainHashTable(capacity=expected_value)
    hash_table["hello"] = "world"
    actual_value = len(hash_table._buckets)
    assert actual_value == expected_value


def test_capacity_should_not_shrink_when_removing_elements():
    expected_value = 100
    hash_table = SeparateChainHashTable(capacity=expected_value)
    hash_table["hello"] = "world"
    del hash_table["hello"]
    actual_value = len(hash_table._buckets)
    assert actual_value == expected_value


def test_should_insert_none_value():
    hash_table = SeparateChainHashTable(capacity=100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.pairs


def test_should_find_value_by_key(hash_table):
    assert hash_table["hello"] == "world"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True


def test_should_raise_error_on_missing_key():
    hash_table = SeparateChainHashTable(capacity=100)
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
    expected_values = [("hello", "world"), (98.6, 37), (False, True)]
    assert hash_table.pairs == expected_values


def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs


def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs


def test_should_get_pairs_of_empty_hash_table():
    assert SeparateChainHashTable(capacity=100).pairs == []


def test_should_return_duplicate_values():
    hash_table = SeparateChainHashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    expected_values = [24, 42, 42]
    assert unordered(hash_table.values) == expected_values


def test_should_get_values(hash_table):
    expected_values = ["world", 37, True]
    assert unordered(hash_table.values) == expected_values


def test_should_get_values_of_empty_hash_table():
    assert SeparateChainHashTable(capacity=100).values == []


def test_should_return_copy_of_values(hash_table):
    assert hash_table.values is not hash_table.values


def test_should_get_keys(hash_table):
    assert hash_table.keys == ["hello", 98.6, False]


def test_should_get_keys_of_empty_hash_table():
    assert SeparateChainHashTable(capacity=100).keys == []


def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys


def test_should_convert_to_dict(hash_table):
    dictionary = dict(hash_table.pairs)
    assert list(dictionary.keys()) == hash_table.keys
    assert list(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == unordered(hash_table.values)


def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        SeparateChainHashTable(capacity=0)


def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        SeparateChainHashTable(capacity=-100)


def test_should_not_create_hashtable_with_wrong_type_capacity():
    with pytest.raises(ValueError):
        SeparateChainHashTable(capacity='100')


def test_should_not_create_hashtable_with_negative_threshold():
    with pytest.raises(ValueError):
        SeparateChainHashTable(load_factor_threshold=-100)


def test_should_not_create_hashtable_with_greater_than_one_threshold():
    with pytest.raises(ValueError):
        SeparateChainHashTable(load_factor_threshold=100)


def test_should_report_capacity(hash_table):
    assert hash_table.capacity == 100


def test_should_report_capacity_of_empty_hash_table():
    assert SeparateChainHashTable(capacity=100).capacity == 100


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
        "SeparateChainHashTable.from_dict({'hello': 'world', 98.6: 37, False: True})",
        "SeparateChainHashTable.from_dict({'hello': 'world', False: True, 98.6: 37})",
        "SeparateChainHashTable.from_dict({98.6: 37, 'hello': 'world', False: True})",
        "SeparateChainHashTable.from_dict({98.6: 37, False: True, 'hello': 'world'})",
        "SeparateChainHashTable.from_dict({False: True, 'hello': 'world', 98.6: 37})",
        "SeparateChainHashTable.from_dict({False: True, 98.6: 37, 'hello': 'world'})",
    }


def test_should_create_hashtable_from_dict():
    expected_capacity = 6
    dictionary = {"hello": "world", 98.6: 37, False: True}
    hash_table = SeparateChainHashTable.from_dict(dictionary)
    assert hash_table.capacity == expected_capacity
    assert hash_table.keys == list(dictionary.keys())
    assert hash_table.pairs == list(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())


def test_should_create_hashtable_from_dict_with_custom_capacity():
    expected_capacity = 100
    dictionary = {"hello": "world", 98.6: 37, False: True}
    hash_table = SeparateChainHashTable.from_dict(dictionary, capacity=100)
    assert hash_table.capacity == expected_capacity
    assert hash_table.keys == list(dictionary.keys())
    assert hash_table.pairs == list(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())


def test_should_compare_equal_to_itself(hash_table):
    assert hash_table == hash_table


def test_should_compare_equal_to_copy(hash_table):
    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()


def test_should_compare_equal_different_key_value_order(hash_table):
    h1 = SeparateChainHashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = SeparateChainHashTable.from_dict({"b": 2, "a": 1, "c": 3})
    assert h1 == h2


def test_should_compare_unequal(hash_table):
    other = SeparateChainHashTable.from_dict({"different": "value"})
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
    h1 = SeparateChainHashTable.from_dict(data, capacity=50)
    h2 = SeparateChainHashTable.from_dict(data, capacity=100)
    assert h1 == h2


def test_should_handle_hash_collisions_with_separate_chaining():
    expected_value = deque([
        Pair(key='first', value='1st'),
        Pair(key='second', value='2nd')])
    with patch("builtins.hash", return_value=24):
        hash_table = SeparateChainHashTable(capacity=100)
        hash_table["first"] = "1st"
        hash_table["second"] = "2nd"
    assert hash_table._buckets[24] == expected_value


def test_should_resize_hash_table_when_capacity_is_full():
    expected_capacity = 32
    hash_table = SeparateChainHashTable(capacity=1)
    for i in range(20):
        hash_table[i] = i
        assert hash_table[i] == i
    assert hash_table.capacity == expected_capacity


def test_should_calculate_correct_load_factor(hash_table):
    expected_load_factor = 0.03
    assert hash_table.load_factor == expected_load_factor


def test_should_retain_insertion_order_and_be_zipable(hash_table):
    expected_value = list(zip(hash_table.keys, hash_table.values))
    assert hash_table.pairs == expected_value
