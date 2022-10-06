"""
Hash Table data structure coded from scratch.
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

    def __setitem__(self, key, value):
        """todo

        Args:
            key: todo.
            value: todo.
        """
        index = hash(key) % len(self)
        self.values[index] = value


    def hash(self, key):
        """Gets index of array for a specific string key.

        Args:
            key: todo.
        """
        length = self.__len__
        return hash(key) % length


# class ArrayList:
#     """todo
#     """
#     pass


# class StringBuilder:
#     """todo
#     """
#     pass
