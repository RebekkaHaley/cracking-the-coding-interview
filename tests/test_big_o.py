"""
Tests for 'Chapter VI: Big O'.
"""

import numpy as np

from cracking_the_coding_interview.big_o import (
    binary_search,
    recursion_example,
    sum_and_product,
    permutation,
    fibonacci,
    fibonacci_memoized,
    fibonacci_seq,
    fibonacci_seq_memoized,
    powers_of_two)

SEARCH_ARRAY = np.array([1, 3, 5, 10, 45, 55, 67, 74, 77, 99])


def test_binary_search_valid_target_not_present():
    target_number = 17
    test_output = binary_search(array=SEARCH_ARRAY, target_num=target_number)
    correct_output = -1
    assert test_output == correct_output


def test_binary_search_valid_first_index():
    target_number = 1
    test_output = binary_search(array=SEARCH_ARRAY, target_num=target_number)
    correct_output = 0
    assert test_output == correct_output


def test_binary_search_valid_last_index():
    target_number = 99
    test_output = binary_search(array=SEARCH_ARRAY, target_num=target_number)
    correct_output = 9
    assert test_output == correct_output


def test_binary_search_valid_middle_index():
    target_number = 55
    test_output = binary_search(array=SEARCH_ARRAY, target_num=target_number)
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


def test_sum_and_product_valid_correct_output():
    assert sum_and_product(numbers=[1, 2, 3, 4, 5]) == (15, 120)


def test_permutation_valid_show_print_false():
    assert permutation(string='abcd', prefix='', show_print=False) == None


def test_permutation_valid_show_print_true():
    assert permutation(string='abcd', prefix='', show_print=True) == None


def test_fibonacci_valid_correct_outputs():
    assert fibonacci(number=-3) == 0
    assert fibonacci(number=3) == 2


def test_fibonacci_memoized_valid_correct_outputs():
    init_number = 3
    init_memo = np.zeros(shape=init_number + 1, dtype=int)
    assert fibonacci_memoized(number=-init_number, memo=init_memo) == 0
    assert fibonacci_memoized(number=init_number, memo=init_memo) == 2


def test_fibonacci_seq_valid_correct_output():
    assert fibonacci_seq(number=10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_seq_memoized_valid_correct_output():
    assert fibonacci_seq_memoized(number=10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_powers_of_two_valid_correct_outputs():
    assert powers_of_two(-999) == 0
    assert powers_of_two(1) == 1
    assert powers_of_two(8) == 8
