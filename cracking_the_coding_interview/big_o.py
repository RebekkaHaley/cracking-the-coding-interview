"""
Functions for the 'Big O' chapter in 'Cracking the Coding Interview'.
"""


def binary_search(array, target_num):
    """Retrieves the index of a target number from a sorted array using the binary search algorithm.

    Used to showcase O(log n) runtime.

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

    Used to showcase O(2**n) runtime.
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

    Used to showcase O(n) runtime.

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


def permutation(string: str, prefix: str, show_print: bool) -> None:
    """Prints all permutations of a given string.

    Used to showcase O((n + 2)!) runtime.

    Args:
        string: Any string.
        prefix: Should be initialised as an empty string: ''.
        show_print: Prints permutations if True.
    """
    if len(string) == 0:
        if show_print:
            print(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i+1:]
            permutation(rem, prefix + string[i], show_print=show_print)


def fibonacci(number: int) -> int:
    """Returns the Nth number in the Fibonacci sequence.

    Used to showcase O(2**n) runtime.
    To calculate big o runtime of recursive calls use: O(branches**depth), where depth is usually as deep as N.

    Args:
        number: Any integer.

    Returns:
        Nth Fibonacci number.
    """
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number=number - 1) + fibonacci(number=number - 2)
