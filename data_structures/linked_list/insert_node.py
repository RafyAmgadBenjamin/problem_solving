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


def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next

        # if node:
        #     print(sep)


# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    temp = head
    # In case empty list
    if not head:
        node = SinglyLinkedListNode(data)
        head = node
    else:
        while temp.next != None:
            temp = temp.next

        node = SinglyLinkedListNode(data)
        temp.next = node

    return head


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    head = linked_list.head
    head = insertNodeAtTail(head, 5)
    head = insertNodeAtTail(head, 15)
    head = insertNodeAtTail(head, 25)
    head = insertNodeAtTail(head, 35)
    head = insertNodeAtTail(head, 45)
    print_singly_linked_list(head)

