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


# tests for __init__()


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


# tests for _resize()


def test_should_resize_empty_array_with_correct_new_capacity():
    expected_capacity = 8
    array_list = ArrayList(capacity=expected_capacity)
    array_list._resize()
    assert array_list.capacity == expected_capacity * 2


def test_should_resize_empty_array_with_empty_new_list():
    expected_capacity = 8
    array_list = ArrayList(capacity=expected_capacity)
    expected_new_list = [None] * (expected_capacity * 2)
    array_list._resize()
    assert array_list.list == expected_new_list


def test_should_resize_populated_array_with_populated_new_list(array_list):
    expected_capacity = 8
    expected_new_list = [None] * (expected_capacity * 2)
    expected_new_list[0] = "world"
    expected_new_list[1] = 37
    expected_new_list[2] = True
    array_list._resize()
    assert array_list.list == expected_new_list


# tests for _check_valid_index()


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


# tests for add()


@pytest.mark.skip
def test_should_add_value_with_valid_index():
    pass


# tests for get()


@pytest.mark.skip
def test_should_get_value_with_valid_index():
    pass


# tests for delete()


@pytest.mark.skip
def test_should_delete_value_with_valid_index():
    pass


# tests for update()


@pytest.mark.skip
def test_should_update_value_with_valid_index():
    pass
