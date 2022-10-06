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
        """Sets item to an index of the array.

        Args:
            key: todo.
            value: todo.
        """
        length = self.__len__()
        index = hash(key) % length
        self.values[index] = value

    def __getitem__(self, key):
        """Gets item from an index of the array.

        Args:
            key: todo.
            value: todo.
        """
        length = self.__len__()
        index = hash(key) % length
        return self.values[index]


# class ArrayList:
#     """todo
#     """
#     pass


# class StringBuilder:
#     """todo
#     """
#     pass
