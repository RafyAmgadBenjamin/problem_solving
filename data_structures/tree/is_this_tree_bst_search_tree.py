""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
from collections import defaultdict
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):

    def In_order(root,values):
        if not root:
            return 
        In_order(root.left, values)
        values.append(root.data)
        In_order(root.right, values)


    values =[]
    In_order(root,values)

    for i in range(len(values)-1):
        if values[i]>=values[i+1]:
            return False
    return  True

