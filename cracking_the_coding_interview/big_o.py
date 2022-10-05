"""
Functions for 'Chapter VI: Big O' in 'Cracking the Coding Interview'.
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


def sum_and_product(numbers):
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
        for i, char in enumerate(string):
            rem = string[0:i] + string[i+1:]
            permutation(rem, prefix + char, show_print=show_print)


def fibonacci(number: int) -> int:
    """Returns the Nth number in the Fibonacci sequence.

    Used to showcase O(2**n) runtime.
    To calculate runtime of recursive calls use: O(branches**depth), where depth is often deep as N.

    Args:
        number: Any integer.

    Returns:
        Nth Fibonacci number.
    """
    if number <= 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number=number - 1) + fibonacci(number=number - 2)


def fibonacci_seq(number) -> list:
    """Calculates each Fibonacci number in sequence until Nth number.

    Args:
        number: Any integer.

    Returns:
        Sequence of Fibonacci numbers up to N.
    """
    return [fibonacci(number=num) for num in range(number)]


def fibonacci_memoized(number: int, memo: list) -> int:
    """Returns the Nth number in the Fibonacci sequence with Memoization.

    Used to showcase O(n) runtime.
    Looking up previously computed and stored values takes a constant time.
    Therefore, we are doing a constant amount of work n times, thus O(n).

    Args:
        number: Any integer.
        memo: Cached previously computed values.

    Returns:
        Nth Fibonacci number.
    """
    if number <= 0:
        return 0
    if number == 1:
        return 1
    if memo[number] > 0:
        return memo[number]
    first_call = fibonacci_memoized(number=number - 1, memo=memo)
    second_call = fibonacci_memoized(number=number - 2, memo=memo)
    memo[number] = first_call + second_call
    return memo[number]


def fibonacci_seq_memoized(number) -> list:
    """Calculates each Fibonacci number in sequence until Nth number with Memoization.

    Args:
        number: Any integer.

    Returns:
        Sequence of Fibonacci numbers up to N.
    """
    init_memo = [0 for _ in range(number + 1)]
    return [fibonacci_memoized(number=num, memo=init_memo) for num in range(number)]


def powers_of_two(number: int) -> int:
    """Returns powers of 2 from 1 through n (inclusive).

    NB: The print statements included in the book's example have been removed.

    Used to showcase O(log n) runtime.
    The number of times we can halve n until we reach 1 is log n.
    Calls that demonstrate elements of decay usually involve log.

    Args:
        number: Any integer.

    Returns:
        Last power of 2 in sequence.
    """
    if number < 1:
        return 0
    if number == 1:
        return 1
    prev = powers_of_two(number=number / 2)
    curr = prev * 2
    return curr
