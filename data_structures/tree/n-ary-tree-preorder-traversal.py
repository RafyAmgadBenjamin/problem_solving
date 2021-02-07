class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node"):
        nodes_vals = []

        def traverse(root):
            if not root:
                return
            nodes_vals.append(root.val)
            for child in root.children:
                traverse(child)

        traverse(root)
        return nodes_vals
