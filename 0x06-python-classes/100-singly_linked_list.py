#!/usr/bin/python3
"""Defines class Node"""


class Node:
    """Sets the data of the Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """get the data of the node - takes one parameter"""
    @property
    def data(self):
        return self.__data

    """set the data of the node"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """Get the reference to the next Node"""
    @property
    def next_node(self):
        return self.__next_node

    """ Validate that next_node is a Node object"""
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines class SinglyLinkedList"""


class SinglyLinkedList:
    """init method - Initialize the head of the linked list"""
    def __init__(self):
        self.head = None

    """Create a new node with the given value"""
    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next_node is not None and value > curr.next_node.data:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    """defines the linked list should be represented as a str"""
    def __str__(self):
        output = ""
        curr = self.head
        first_iteration = True
        while curr is not None:
            if not first_iteration:
                output += "\n"
            output += str(curr.data)
            curr = curr.next_node
            first_iteration = False
        return output
