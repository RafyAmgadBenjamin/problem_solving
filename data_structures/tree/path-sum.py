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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def traverse(root, targetSum):
            if not root:
                return False

            if not root.right and not root.left:
                return targetSum == root.val

            return traverse(root.left, targetSum - root.val) or traverse(root.right, targetSum - root.val)

        return traverse(root, targetSum)


if __name__ == "__main__":
    t = Tree()
    int_root = TreeNode()
    tree = Tree()
    root = None
    values = [1, 2]
    for i in values:
        root = tree.insert(root=root, val=i)
    s = Solution()
    print(s.hasPathSum(root, 1))
