"""
StringBuilder data structure coded from scratch.
"""

from io import StringIO


class StringBuilder:
    """StringBuilder data structure using list and join().
    """
    def __init__(self):
        self.memory = []

    def add(self, string: str):
        """Appends string to StringBuilder.

        Args:
            string: Any string.
        """
        self.memory.append(string)

    def __str__(self):
        """Returns fully built string with all appended strings.
        """
        return "".join(self.memory)


class StringBuilderIO:
    """StringBuilder data structure using StringIO.
    """
    def __init__(self):
        self.memory = StringIO()

    def add(self, string: str):
        """Appends string to StringBuilder.

        Args:
            string: Any string.
        """
        self.memory.write(string)

    def __str__(self):
        """Returns fully built string with all appended strings.
        """
        return self.memory.getvalue()
