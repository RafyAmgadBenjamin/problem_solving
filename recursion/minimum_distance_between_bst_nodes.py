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
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_val = 9999999
        self.values = []

        def dfs(root: TreeNode):
            self.values.append(root.val)
            if root.right:
                dfs(root.right)
            if root.left:
                dfs(root.left)

        dfs(root)
        for i in range(len(self.values)):
            # for j in range(len(values)):
            j = i + 1
            while j < len(self.values):
                value_diff = abs(self.values[i] - self.values[j])
                if self.min_val > value_diff:
                    self.min_val = value_diff
                j += 1

        return self.min_val


tree = Tree()
root = None
values = [90, 69, 49, 89, 52]
for i in values:
    root = tree.insert(root=root, val=i)
sol = Solution()
print(sol.minDiffInBST(root))
