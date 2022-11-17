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
    NB: For the sake of simplicity, data is assumed to be integers only.
    """
    def __init__(self) -> None:
        self.head = None

    def insert_head(self, data: int=None) -> None:
        """Inserts a new node to the linked list at the head.

        Args:
            data: Any integer.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data: int=None) -> None:
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

    def insert_after(self, data: int, target_data: int) -> None:
        """Inserts a new node after the node containing target data.
        NB: Raises exception if target is not found or list is empty.

        Args:
            data: Any integer to be assigned to new node.
            target_data: Integer associated with target node.
        """
        new_node = Node(data)
        if self.head:
            current = self.head
            while (current.next):
                if current.data == target_data:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            raise ValueError("Target node not found.")
        else:
            raise ValueError("Linked list is empty.")

    def print_list(self) -> None:
        """Prints linked list nodes in order from head to tail.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def visualise(self) -> None:
        """Prints linked list nodes in a single line.
        """
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        nodes.append("None")
        print(" -> ".join(nodes))
