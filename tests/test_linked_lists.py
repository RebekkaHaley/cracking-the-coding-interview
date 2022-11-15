"""
Tests for section '2. Linked Lists' of 'Chapter IX: Interview Questions'.
"""

import pytest

from ctci.linked_lists import Node


def test_should_initialise_node_with_data():
    node = Node(data=10)
    assert node.next == None
    assert node.data == 10


def test_should_initialise_node_without_data_as_none():
    node = Node()
    assert node.next == None
    assert node.data == None


@pytest.mark.skip
def test_should_append_new_node_to_tail_node():
    pass
