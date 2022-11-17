"""
Tests for section '2. Linked Lists' of 'Chapter IX: Interview Questions'.
"""

from pytest import fixture, raises
from unittest.mock import patch, call

from ctci.linked_lists import Node, SinglyLinkedList


@fixture
def linked_list():
    sample_list = SinglyLinkedList()
    sample_list.insert_head(data=12)
    sample_list.insert_head(data=11)
    sample_list.insert_head(data=10)
    return sample_list


def test_should_populate_single_node_with_data():
    node = Node(data=10)
    assert node.data == 10


def test_should_populate_single_node_without_data():
    node = Node()
    assert node.data == None


def test_should_initialise_single_node_without_next():
    node = Node()
    assert node.next == None


def test_should_initialise_linked_list_without_head():
    l_list = SinglyLinkedList()
    assert l_list.head == None


def test_should_populate_empty_linked_list_with_data_node():
    l_list = SinglyLinkedList()
    l_list.head = Node(10)
    assert l_list.head.data == 10


def test_should_insert_node_to_empty_linked_list_at_head():
    l_list = SinglyLinkedList()
    l_list.insert_head()
    assert l_list.head.data == None
    assert l_list.head.next == None


def test_should_insert_data_node_to_empty_linked_list_at_head():
    l_list = SinglyLinkedList()
    l_list.insert_head(data=10)
    assert l_list.head.data == 10
    assert l_list.head.next == None


def test_should_insert_nodes_to_populated_linked_list_at_head(linked_list):
    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 11
    assert linked_list.head.next.next.data == 12
    assert linked_list.head.next.next.next == None


def test_should_insert_node_to_empty_linked_list_at_tail():
    l_list = SinglyLinkedList()
    l_list.insert_tail()
    assert l_list.head.data == None
    assert l_list.head.next == None


def test_should_insert_data_node_to_empty_linked_list_at_tail():
    l_list = SinglyLinkedList()
    l_list.insert_tail(data=10)
    assert l_list.head.data == 10
    assert l_list.head.next == None


def test_should_insert_nodes_to_populated_linked_list_at_tail():
    l_list = SinglyLinkedList()
    l_list.insert_tail(data=10)
    l_list.insert_tail(data=11)
    l_list.insert_tail(data=12)
    assert l_list.head.data == 10
    assert l_list.head.next.data == 11
    assert l_list.head.next.next.data == 12
    assert l_list.head.next.next.next == None


def test_should_raise_error_when_inserting_after_to_an_empty_linked_list():
    l_list = SinglyLinkedList()
    with raises(ValueError):
        l_list.insert_after(data=1, target_data=1)


def test_should_raise_error_when_inserting_after_using_a_missing_target(linked_list):
    with raises(ValueError):
        linked_list.insert_after(data=1, target_data=1)


def test_should_insert_node_after_target_in_a_populated_linked_list(linked_list):
    linked_list.insert_after(data=99, target_data=11)
    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 11
    assert linked_list.head.next.next.data == 99
    assert linked_list.head.next.next.next.data == 12
    assert linked_list.head.next.next.next.next == None


def test_should_raise_error_when_deleting_from_an_empty_linked_list():
    l_list = SinglyLinkedList()
    with raises(ValueError):
        l_list.delete_node(target_data=0)


def test_should_raise_error_when_deleting_using_a_missing_target(linked_list):
    with raises(ValueError):
        linked_list.delete_node(target_data=0)


def test_should_delete_node_from_list_head(linked_list):
    linked_list.delete_node(target_data=10)
    assert linked_list.head.data == 11
    assert linked_list.head.next.data == 12
    assert linked_list.head.next.next == None


def test_should_delete_node_from_middle_of_list(linked_list):
    linked_list.delete_node(target_data=11)
    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 12
    assert linked_list.head.next.next == None


def test_should_delete_first_duplicate():
    l_list = SinglyLinkedList()
    l_list.insert_head(data=10)
    l_list.insert_head(data=11)
    l_list.insert_head(data=10)
    l_list.delete_node(target_data=10)
    assert l_list.head.data == 11
    assert l_list.head.next.data == 10
    assert l_list.head.next.next == None


def test_should_print_linked_list(linked_list):
    with patch('builtins.print') as print_output:
        linked_list.print_list()
    assert print_output.mock_calls == [call(10), call(11), call(12)]


def test_should_visualise_linked_list(linked_list):
    with patch('builtins.print') as print_output:
        linked_list.visualise()
    assert print_output.mock_calls == [call("10 -> 11 -> 12 -> None")]
