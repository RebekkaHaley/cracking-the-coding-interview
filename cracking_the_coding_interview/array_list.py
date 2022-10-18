"""
ArrayList data structure coded from scratch.
"""

from typing import Any


class ArrayList:
    """ArrayList data structure.

    Args:
        capacity: Maximum memory capacity. Default is 8.
    """
    def __init__(self, capacity: int=8):
        self.capacity = capacity
        self.list = [None] * self.capacity
        self.current_size = 0

    def _resize(self):
        """Doubles array (n*2) when maximum capacity is reached.
        """
        new_capacity = self.capacity * 2
        new_list = [None] * new_capacity
        for i, value in enumerate(self.list):
            new_list[i] = value
        self.capacity = new_capacity
        self.list = new_list

    def _check_valid_index(self, index):
        """Raises error if given input is not a valid index.

        Args:
            index: An index of the array.
        """
        if not isinstance(index, int):
            raise ValueError("Index must be an int type")
        if index >= self.capacity or index < 0:
            raise IndexError('Invalid index')

    def add(self, value: Any):
        """Appends given value to array at last index.

        Args:
            value: Any value to input into array.
        """
        if self.current_size >= self.capacity:
            self._resize()
        self.list[self.current_size] = value
        self.current_size += 1

    def get(self, index: int) -> Any:
        """Retrieves value corresponding to given index.

        Args:
            index: An index of the array.
        """
        self._check_valid_index(index=index)
        return self.list[index]

    def delete(self, index: int):
        """Removes value corresponding to given index and left-shifts all subsequent values.

        Args:
            index: An index of the array.
        """
        self._check_valid_index(index=index)
        for i in range(index, self.capacity):
            self.list[i] = self.list[i + 1]
        self.current_size -= 1

    def update(self, index: int, value: Any):
        """Replaces value corresponding to given index with new given value.

        Args:
            index: An index of the array.
            value: Any value to input into array.
        """
        self._check_valid_index(index=index)
        self.list[index] = value
