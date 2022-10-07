"""
Hash Table data structure coded from scratch. TODO: Code is still a WIP.
"""

BLANK = object()


class HashTable:
    """Simple implementation of a hash table data structure using Python from scratch.

    Args:
        capacity: Size used to initiate array with empty values.
    """
    def __init__(self, capacity: int):
        self.values = capacity * [BLANK]

    def __len__(self):
        """Returns capacity of array.
        """
        return len(self.values)

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
        self.values[self._index(key=key)] = value

    def __getitem__(self, key):
        """Gets item from an index of the array.

        Args:
            key (todo): todo.
            value (todo): todo.
        """
        value = self.values[self._index(key=key)]
        if value is BLANK:
            raise KeyError(key)
        return value

    def __delitem__(self, key):
        """todo.

        Args:
            key (todo): todo.
        """
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    def _index(self, key) -> int:
        """Calculates index using Python's in-built hashing function formula.

        Args:
            key (todo): todo.

        Returns
            An index of the hash table.
        """
        length = self.__len__()
        return hash(key) % length

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


# class ArrayList:
#     """todo
#     """
#     pass


# class StringBuilder:
#     """todo
#     """
#     pass
