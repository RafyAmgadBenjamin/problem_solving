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


def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next

        # if node:
        #     fptr.write(sep)


# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    tmp = llist
    # In case it is Empty
    if not tmp:
        node = SinglyLinkedListNode(data)
        llist = node
    else:
        node = SinglyLinkedListNode(data)
        tmp = llist
        llist = node
        llist.next = tmp
    return llist


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    head = linked_list.head
    head = insertNodeAtHead(head, 5)
    head = insertNodeAtHead(head, 15)
    head = insertNodeAtHead(head, 25)
    head = insertNodeAtHead(head, 35)
    head = insertNodeAtHead(head, 45)
    print_singly_linked_list(head)
