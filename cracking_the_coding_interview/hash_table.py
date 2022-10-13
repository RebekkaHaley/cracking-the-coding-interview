"""
Hash Table data structure coded from scratch. TODO: Code is still a WIP.

Resources:
- [Build a Hash Table in Python With TDD](https://realpython.com/python-hash-table/)
"""

from typing import NamedTuple, Any

DELETED = object()


class Pair(NamedTuple):
    """Representation of a key-value pair in a simple hash table.
    """
    key: Any
    value: Any


class HashTable:
    """Simple implementation of a hash table data structure using Python from scratch.

    Args:
        capacity: Size used to initiate array with empty values. Default is 8.
    """
    def __init__(self, capacity: int=8):
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an int type")
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        self._slots = capacity * [None]

    def __len__(self):
        """Returns length of hash table, rather than maximum capacity.
        """
        return len(self.pairs)

    def __setitem__(self, key: Any, value: Any):
        """Inserts a key-value pair to an index.

        Args:
            key: A unique identifier of the key-value pair.
            value: An identified data.
        """
        for index, pair in self._probe(key):
            if pair is DELETED:
                continue
            if pair is None or pair.key == key:
                self._slots[index] = Pair(key, value)
                break
        else:
            self._resize_and_rehash()
            self[key] = value

    def __getitem__(self, key: Any):
        """Gets a value by a given key from an index.

        Args:
            key: A unique identifier of the key-value pair.
        """
        for _, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __delitem__(self, key: Any):
        """Removes a previously inserted key-value pair from an index.

        Args:
            key: A unique identifier of the key-value pair.
        """
        for index, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                self._slots[index] = DELETED
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

    def _index(self, key: Any) -> int:
        """Calculates index using Python's in-built hashing function formula.

        Args:
            key: A unique identifier of the key-value pair.

        Returns:
            An index of the hash table.
        """
        return hash(key) % self.capacity

    def _probe(self, key: Any):
        """Visits hash table slots.

        Args:
            key: A unique identifier of the key-value pair.
        """
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._slots[index]
            index = (index + 1) % self.capacity

    def _resize_and_rehash(self):
        """Increases hash table size and rehashes all key-value pairs using a copy.
        """
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._slots = copy._slots

    def get(self, key: Any, default: str=None):
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
        return {pair for pair in self._slots if pair not in (None, DELETED)}

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
            capacity: Optional. Uses length of given dict as default.
        """
        if not capacity:
            capacity = len(dictionary)
        hash_table = cls(capacity)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
