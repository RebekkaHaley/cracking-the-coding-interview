"""
Functions for the 'Big O' chapter in 'Cracking the Coding Interview'.
"""


def binary_search(array, target_num):
    """Retrieves the index of a target number from a sorted array using the binary search algorithm.

    Used to showcase O(log n) run time.

    Args:
        array (list of int): An array of sorted numbers.
        target_num (int): Target number of binary search.

    Returns:
        int: Index of target number.
    """
    mid_index = 0
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:
        mid_index = (high_index + low_index) // 2
        suggested_num = array[mid_index]
        if target_num > suggested_num:  # if target is greater than, ignore left half
            low_index = mid_index + 1
        elif target_num < suggested_num:  # if target is less than, ignore right half
            high_index = mid_index - 1
        else:
            return mid_index
    return -1  # if code reaches this point, then target was not present


def recursion_example(number):
    """Calculates sum of recursively generated nodes.

    Used to showcase O(2**n) run time.
    The tree has depth: 'number'. The total number of nodes is: (2**n)-1, where n is 'number'.

    Args:
        number (int): A positive integer.

    Returns:
        int: Calculated sum.
    """
    if number <= 1:
        return 1
    return recursion_example(number=number-1) + recursion_example(number=number-1)


def log_n_example(numbers):
    """Calculates total sum and total product of given list of numbers.

    Used to showcase O(n) run time.

    Args:
        numbers (list of int): List of integers.

    Returns:
        Tuple of ints:
            int: Total sum of integers.
            int: Total product of integers.
    """
    total_sum = 0
    total_product = 1
    for number in numbers:
        total_sum += number
    for number in numbers:
        total_product *= number
    return total_sum, total_product
