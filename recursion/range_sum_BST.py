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
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0
        # Recurant relation
        # if root.right and root.left:
        #     return self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
        def dfs(node):
            if node.right:
                dfs(node.right)
            if node.left:
                dfs(node.left)

            # Stopping condition
            if (low <= node.val <= high) and node.val != None:
                self.ans += node.val

        dfs(root)
        return self.ans


tree = Tree()
root = None
values = [10, 5, 15, 3, 7, 18]
for i in values:
    root = tree.insert(root=root, val=i)


sol = Solution()
res = sol.rangeSumBST(root, 7, 15)

print(res)
