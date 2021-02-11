# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def insert(self, root: TreeNode, val: int = -1):
        if root == None:
            return TreeNode(val)
        if val > root.val and root.val != None:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        return root


class Solution:
    def find_root(self, root, val):
        self.root = None

        def traverse(root, val):
            if not root:
                return

            if root.val == val:
                self.root = root

            traverse(root.left, val)
            traverse(root.right, val)

        traverse(root, val)
        return self.root

    def find_subtree(self, root):
        path = []

        def traverse(root):
            if not root:
                return
            path.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return path

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.find_root(root, val)


if __name__ == "__main__":
    t = Tree()
    int_root = TreeNode()
    tree = Tree()
    root = None
    values = [4, 2, 7, 1, 3]
    for i in values:
        root = tree.insert(root=root, val=i)
    s = Solution()
    root = s.searchBST(root, 2)
    print(vars(root))
