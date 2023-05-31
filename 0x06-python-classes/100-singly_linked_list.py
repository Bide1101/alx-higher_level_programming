#!/usr/bin/python3
"""Defines class Node"""


class Node:
    """Sets the data of the Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data of the node - takes one parameter"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the reference to the next Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Validate that next_node is a Node object"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines class SinglyLinkedList"""


class SinglyLinkedList:
    def __init__(self):
        """init method - Initialize the head of the linked list"""
        self.head = None

    def sorted_insert(self, value):
        """Create a new node with the given value"""
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
