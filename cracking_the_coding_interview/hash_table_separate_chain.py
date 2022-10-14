"""
Hash Table using separate chaining to handle collisions.
Full tutorial completed.

Resources:
- [Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/)
"""

from typing import NamedTuple, Any
from collections import deque


class Pair(NamedTuple):
    """Representation of a key-value pair in a simple hash table.
    """
    key: Any
    value: Any


class SeparateChainHashTable:
    """Hash table using separate chaining to handle collisions.

    Args:
        capacity: Size used to initiate array with empty values. Default is 8.
        load_factor_threshold: Determines when to resize and rehash. Default is 0.6.
    """
    def __init__(self, capacity: int=8, load_factor_threshold: float=0.6):
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an int type")
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        if not 0 < load_factor_threshold <= 1:
            raise ValueError("Load factor must be a number between (0, 1]")
        self._keys = []
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold

    def __len__(self) -> int:
        """Returns length of hash table, rather than maximum capacity.
        """
        return len(self.pairs)

    def __setitem__(self, key: Any, value: Any):
        """Inserts a key-value pair to an index.

        Args:
            key: A unique identifier of the key-value pair.
            value: An identified data.
        """
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            bucket.append(Pair(key, value))
            self._keys.append(key)

    def __getitem__(self, key: Any):
        """Gets a value by a given key from an index.

        Args:
            key: A unique identifier of the key-value pair.
        """
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __delitem__(self, key: Any):
        """Removes a previously inserted key-value pair from an index.

        Args:
            key: A unique identifier of the key-value pair.
        """
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                self._keys.remove(key)
                break
        else:
            raise KeyError(key)

    def __contains__(self, key: Any) -> bool:
        """Determines whether a given key has an associated value in the hash table.

        Args:
            key: A unique identifier of the key-value pair.
        """
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self):
        """Returns an iterator object.
        """
        yield from self.keys

    def __str__(self) -> str:
        """Returns string representation of hash table.

        Used when printed onto the standard output.
        """
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self) -> repr:
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

    def _index(self, key: Any) -> int:
        """Calculates index using Python's in-built hashing function formula.

        Args:
            key: A unique identifier of the key-value pair.

        Returns:
            An index of the hash table.
        """
        return hash(key) % self.capacity

    def _resize_and_rehash(self):
        """Increases hash table size and rehashes all key-value pairs using a copy.
        """
        copy = SeparateChainHashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._buckets = copy._buckets

    def get(self, key: Any, default: str=None) -> Any:
        """Gets a value by a given key from an index.

        Args:
            key: A unique identifier of the key-value pair.
            default: Optional.
        """
        try:
            return self[key]
        except KeyError:
            return default

    def copy(self):
        """Returns a new copy of a hash table instance.
        """
        return SeparateChainHashTable.from_dict(dict(self.pairs), self.capacity)

    @property
    def capacity(self) -> int:
        """Returns maximum capacity.
        """
        return len(self._buckets)

    @property
    def keys(self) -> dict:
        """Returns all keys.
        """
        return self._keys.copy()

    @property
    def values(self) -> list:
        """Returns all values.
        """
        return [self[key] for key in self.keys]

    @property
    def pairs(self) -> dict:
        """Returns shallow copy of all key-value pairs.
        """
        return [(key, self[key]) for key in self.keys]

    @property
    def load_factor(self) -> float:
        """Calculates the load factor.

        NB: Load factor is the ratio of the number of currently occupied slots vs total slots.
        """
        return len(self) / self.capacity

    @classmethod
    def from_dict(cls, dictionary: dict, capacity: int=None):
        """Creates a hash table using the given dictionary.

        Args:
            dictionary: Key-value pairs that are copied to new hash table.
            capacity: Optional. Uses length of given dict as default.
        """
        if not capacity:
            capacity = len(dictionary)
        hash_table = cls(capacity)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
