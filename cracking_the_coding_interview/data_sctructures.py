"""
Data structures coded from scratch.
"""


class HashTable:
    """Simple implementation of a hash table data structure using Python from scratch.

    Args:
        capacity: Size used to initiate array with empty values.
    """
    def __init__(self, capacity: int):
        self.values = capacity * [None]

    def __len__(self):
        """Returns capacity of array.
        """
        return len(self.values)

    def hash(self, key):
        """Gets index of array for a specific string key.
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
