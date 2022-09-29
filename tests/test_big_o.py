"""
Tests for code related to the 'Big O' chapter in 'Cracking the Coding Interview'.
"""

import numpy as np

from cracking_the_coding_interview.big_o import binary_search, recursion_example

ARRAY = np.array([1, 3, 5, 10, 45, 55, 67, 74, 77, 99])


def test_binary_search_valid_target_not_present():
    target_number = 17
    test_output = binary_search(array=ARRAY, target_num=target_number)
    correct_output = -1
    assert test_output == correct_output


def test_binary_search_valid_first_index():
    target_number = 1
    test_output = binary_search(array=ARRAY, target_num=target_number)
    correct_output = 0
    assert test_output == correct_output


def test_binary_search_valid_last_index():
    target_number = 99
    test_output = binary_search(array=ARRAY, target_num=target_number)
    correct_output = 9
    assert test_output == correct_output


def test_binary_search_valid_middle_index():
    target_number = 55
    test_output = binary_search(array=ARRAY, target_num=target_number)
    correct_output = 5
    assert test_output == correct_output


def todo_recursion_example():
    pass
