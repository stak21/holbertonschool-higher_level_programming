#!/usr/bin/python3
"""Write a Node class for a singly linked list"""


class Node:
    """This class will create nodes for a linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        if type(self.data) is not int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is type(self):
            self.__next_node = value
        else:
            raise TypeError("next_node must be an integer")


class SinglyLinkedList:
    """This class will create a singly linked list using Node"""
    def __init__(self):
        self.__head = None

    def __repr__(self):
        ret_str = ""
        while self.__head is not None:
            ret_str += str(self.__head.data) + '\n'
            self.__head = self.__head.next_node
        return ret_str[0:-1]

    def sorted_insert(self, value):
        cur = self.__head
        if self.__head is None:
            self.__head = Node(value)
            return

        if self.__head.next_node is None:
            self.__head.next_node = Node(value, None)
            return
        if self.__head.data > value:
            self.__head = Node(value, self.__head)
            return

        while self.__head is not None:
            if self.__head.next_node and value < self.__head.next_node.data:
                self.__head.next_node = Node(value, self.__head.next_node)
                self.__head = cur
                return
            elif self.__head.next_node is None:
                self.__head.next_node = Node(value)
                self.__head = cur
                return
            else:
                self.__head = self.__head.next_node
