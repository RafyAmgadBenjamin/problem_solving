#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next


# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    temp = head
    # Handle the first position
    if position == 0:
        head = temp.next
    else:
        for _ in range(position - 1):
            temp = temp.next

        deleted_node = temp.next
        temp.next = deleted_node.next
    if not temp:
        return None
    return head


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_node(16)
    linked_list.insert_node(13)
    linked_list.insert_node(7)
    print_singly_linked_list(linked_list.head)
    new_head = deleteNode(linked_list.head, 0)
    new_head = deleteNode(new_head, 0)
    new_head = deleteNode(new_head, 0)
    print_singly_linked_list(new_head)
