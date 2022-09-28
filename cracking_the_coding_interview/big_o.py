"""
Code for the 'Big O' chapter in 'Cracking the Coding Interview'.
"""


def binary_search(array, target_num):
    """Retrieves the index of a target number from a sorted array using the binary search algorithm.

    Used to showcase O(log n) run time.

    Args:
        array (numpy.ndarray of int): An array of sorted numbers.
        target_num (int): Target number of binary search.
    """
    mid_index = 0
    low_index = 0
    high_index = len(array)
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
