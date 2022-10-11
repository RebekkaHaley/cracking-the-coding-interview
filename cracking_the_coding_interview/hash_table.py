"""
Hash Table data structure coded from scratch. TODO: Code is still a WIP.

Resources:
- [Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/)
"""

from typing import NamedTuple, Any


class Pair(NamedTuple):
    """Representation of a key-value pair in a simple hash table.
    """
    key: Any
    value: Any


class HashTable:
    """Simple implementation of a hash table data structure using Python from scratch.

    Args:
        capacity: Size used to initiate array with empty values.
    """
    def __init__(self, capacity: int):
        self.pairs = capacity * [None]

    def __len__(self):
        """Returns capacity of array.
        """
        return len(self.pairs)

    def __contains__(self, key):
        """todo.

        Args:
            key (todo): todo.
        """
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __setitem__(self, key, value):
        """Sets item to an index of the array.

        Args:
            key (todo): todo.
            value (todo): todo.
        """
        self.pairs[self._index(key=key)] = Pair(key, value)

    def __getitem__(self, key):
        """Gets item from an index of the array.

        Args:
            key (todo): todo.
            value (todo): todo.
        """
        pair = self.pairs[self._index(key=key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __delitem__(self, key):
        """todo.

        Args:
            key (todo): todo.
        """
        if key in self:
            self.pairs[self._index(key=key)] = None
        else:
            raise KeyError(key)

    def _index(self, key) -> int:
        """Calculates index using Python's in-built hashing function formula.

        Args:
            key (todo): todo.

        Returns
            An index of the hash table.
        """
        return hash(key) % len(self)

    def get(self, key, default=None):
        """todo.

        Args:
            key (todo): todo.
            default (str): Optional.
        """
        try:
            return self[key]
        except KeyError:
            return default
