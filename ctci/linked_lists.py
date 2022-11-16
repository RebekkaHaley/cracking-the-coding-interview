"""
Functions for section '2. Linked Lists' of 'Chapter IX: Interview Questions'.
"""


class Node():
    """Single node of a Singly Linked List.

    Args:
        data: Any integer.
    """
    def __init__(self, data: int=None) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList():
    """A Singly Linked List.
    """
    def __init__(self) -> None:
        self.head = None

    def insert(self, data: int=None) -> None:
        """Inserts a new node to the linked list at the tail.

        Args:
            data: Any integer.
        """
        new_node = Node(data)
        if self.head:
            current = self.head
            while (current.next):  # searches for tail node
                current = current.next
            current.next = new_node  # inserts at tail
        else:
            self.head = new_node

    def print_list(self) -> None:
        """Prints linked list nodes in order from head to tail.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next
