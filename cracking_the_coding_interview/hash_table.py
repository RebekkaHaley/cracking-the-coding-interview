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
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an int type")
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        self._slots = capacity * [None]

    def __len__(self):
        """Returns length of hash table, rather than maximum capacity.
        """
        return len(self.pairs)

    def __setitem__(self, key, value):
        """Sets item to an index of the array.

        Args:
            key (todo): todo.
            value (todo): todo.
        """
        self._slots[self._index(key=key)] = Pair(key, value)

    def __getitem__(self, key):
        """Gets item from an index of the array.

        Args:
            key (todo): todo.
            value (todo): todo.
        """
        pair = self._slots[self._index(key=key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __delitem__(self, key):
        """todo.

        Args:
            key (todo): todo.
        """
        if key in self:
            self._slots[self._index(key=key)] = None
        else:
            raise KeyError(key)

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

    def __iter__(self):
        """todo.
        """
        yield from self.keys

    def __str__(self):
        """Returns string representation of hash table.

        Used when printed onto the standard output.
        """
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self):
        """Returns canonical string representation of hash table.
        """
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other) -> bool:
        """Updates hash table to equal itself, its copy, or instances with the same key-value pairs.
        """
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    def _index(self, key) -> int:
        """Calculates index using Python's in-built hashing function formula.

        Args:
            key (todo): todo.

        Returns:
            An index of the hash table.
        """
        return hash(key) % self.capacity

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

    def copy(self):
        """Returns a new copy of a hash table instance.
        """
        return HashTable.from_dict(dict(self.pairs), self.capacity)

    @property
    def capacity(self):
        """Returns maximum capacity.
        """
        return len(self._slots)

    @property
    def pairs(self):
        """Returns shallow copy of all key-value pairs.
        """
        return {pair for pair in self._slots if pair}

    @property
    def values(self):
        """Returns all values.
        """
        return [pair.value for pair in self.pairs]

    @property
    def keys(self):
        """Returns all keys.
        """
        return {pair.key for pair in self.pairs}

    @classmethod
    def from_dict(cls, dictionary: dict, capacity: int=None):
        """Creates a hash table using the given dictionary.

        Args:
            dictionary: Key-value pairs that are copied to new hash table.
            capacity: Optional. Overrides default capacity.
        """
        if not capacity:
            capacity = len(dictionary) * 10
        hash_table = cls(capacity)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
