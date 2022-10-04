"""
Tests for code related to the 'Big O' chapter in 'Cracking the Coding Interview'.
"""

import numpy as np

from cracking_the_coding_interview.big_o import binary_search, recursion_example, log_n_example, permutation

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


def test_recursion_example_valid_single():
    test_result = recursion_example(number=1)
    assert test_result == 1


def test_recursion_example_valid_multi():
    test_result = recursion_example(number=6)
    assert test_result == 32


def test_recursion_example_valid_negative():
    test_result = recursion_example(number=-999)
    assert test_result == 1


def test_log_n_example_valid():
    assert log_n_example(numbers=[1, 2, 3, 4, 5]) == (15, 120)


def test_permutation_valid():
    return 'todo'
