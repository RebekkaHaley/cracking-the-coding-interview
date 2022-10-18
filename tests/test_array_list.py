"""
Tests for ArrayList data structure coded from scratch.
"""

import pytest

from cracking_the_coding_interview.array_list import ArrayList


@pytest.fixture
def array_list():
    sample_array = ArrayList(capacity=8)
    sample_array.add("world")
    sample_array.add(37)
    sample_array.add(True)
    return sample_array


def test_should_create_empty_array_with_empty_list():
    expected_capacity = 8
    expected_list = [None] * expected_capacity
    array_list = ArrayList(capacity=expected_capacity)
    assert array_list.list == expected_list


def test_should_create_empty_array_with_zero_current_size():
    expected_capacity = 8
    expected_current_size = 0
    array_list = ArrayList(capacity=expected_capacity)
    assert array_list.current_size == expected_current_size


def test_should_create_empty_array_with_correct_capacity():
    expected_capacity = 100
    array_list = ArrayList(capacity=expected_capacity)
    assert array_list.capacity == expected_capacity


def test_should_resize_empty_array_with_correct_new_capacity():
    starting_capacity = 8
    expected_capacity = starting_capacity * 2
    array_list = ArrayList(capacity=starting_capacity)
    array_list._resize()
    assert array_list.capacity == expected_capacity


def test_should_resize_empty_array_with_empty_new_list():
    starting_capacity = 8
    array_list = ArrayList(capacity=starting_capacity)
    expected_new_list = [None] * (starting_capacity * 2)
    array_list._resize()
    assert array_list.list == expected_new_list


def test_should_resize_populated_array_with_populated_new_list(array_list):
    starting_capacity = 8
    expected_new_list = [None] * (starting_capacity * 2)
    expected_new_list[0] = "world"
    expected_new_list[1] = 37
    expected_new_list[2] = True
    array_list._resize()
    assert array_list.list == expected_new_list


def test_should_not_raise_error_with_valid_index(array_list):
    array_list._check_valid_index(index=1)


def test_should_raise_error_with_str_dtype_index(array_list):
    with pytest.raises(ValueError):
        array_list._check_valid_index(index="100")


def test_should_raise_error_with_float_dtype_index(array_list):
    with pytest.raises(ValueError):
        array_list._check_valid_index(index=1.0)


def test_should_raise_error_with_index_larger_than_capacity(array_list):
    with pytest.raises(IndexError):
        array_list._check_valid_index(index=100)


def test_should_raise_error_with_negative_index(array_list):
    with pytest.raises(IndexError):
        array_list._check_valid_index(index=-100)


def test_should_add_value_with_valid_index(array_list):
    expected_capacity = 8
    expected_list = [None] * (expected_capacity)
    expected_list[0] = "world"
    expected_list[1] = 37
    expected_list[2] = True
    expected_list[3] = "new value"
    expected_current_size = 4
    array_list.add(value="new value")
    assert array_list.list == expected_list
    assert array_list.current_size == expected_current_size


def test_should_add_value_to_full_capacity_array_using_resize():
    starting_capacity = 2
    expected_capacity = starting_capacity * 2
    expected_list = ["1st", "2nd", "3rd", None]
    array_list = ArrayList(capacity=starting_capacity)
    array_list.add("1st")
    array_list.add("2nd")
    array_list.add("3rd")
    assert array_list.capacity == expected_capacity
    assert array_list.list == expected_list


def test_should_get_value_with_valid_index(array_list):
    assert array_list.get(index=0) == "world"
    assert array_list.get(index=1) == 37
    assert array_list.get(index=2) == True


def test_should_delete_value_with_valid_index(array_list):
    expected_capacity = 8
    expected_list = [None] * (expected_capacity)
    expected_list[0] = "world"
    expected_list[1] = True
    expected_current_size = 2
    array_list.delete(index=1)
    assert array_list.list == expected_list
    assert array_list.current_size == expected_current_size


def test_should_update_value_with_valid_index(array_list):
    expected_capacity = 8
    expected_list = [None] * (expected_capacity)
    expected_list[0] = "world"
    expected_list[1] = "new value"
    expected_list[2] = True
    expected_current_size = 3
    array_list.update(index=1, value="new value")
    assert array_list.list == expected_list
    assert array_list.current_size == expected_current_size
