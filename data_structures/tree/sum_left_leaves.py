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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0

        def get_sum(root: TreeNode):
            if not root:
                return

            if root.left:
                if not root.left.left and not root.left.right:
                    self.sum += root.left.val

            get_sum(root.left)
            get_sum(root.right)

        get_sum(root)
        return self.sum


if __name__ == "__main__":
    t = Tree()
    int_root = TreeNode()
    tree = Tree()
    root = None
    values = [3, 9, 20, 15, 7]
    for i in values:
        root = tree.insert(root=root, val=i)
    s = Solution()
    print(s.sumOfLeftLeaves(root))
