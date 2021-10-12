class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.node_sum = 0
        # self.node_sum += root.val
        self.tilt_nodes = []

        def dfs_sum(root):
            if root.right:
                self.node_sum += root.right.val
                dfs_sum(root.right)
            if root.left:
                self.node_sum += root.left.val
                dfs_sum(root.left)

        def dfs(root):
            right_branch = 0
            left_branch = 0
            if root.right:
                dfs_sum(root.right)
                self.node_sum += root.right.val
                right_branch = self.node_sum
                self.node_sum = 0
                dfs(root.right)
            if root.left:
                dfs_sum(root.left)
                self.node_sum += root.left.val
                left_branch = self.node_sum
                self.node_sum = 0
                dfs(root.left)
            self.tilt_nodes.append(abs(right_branch - left_branch))

        dfs(root)
        # dfs_sum(root.right)
        # self.node_sum += root.right.val
        # print(self.node_sum)
        # self.node_sum = 0
        # dfs_sum(root.left)
        # self.node_sum += root.left.val
        # print(self.node_sum)
        # self.node_sum = 0
        # I need to add the sum of root.right manually
        return self.tilt_nodes


tree = Tree()
root = None
values = [1, 2, 3]
for i in values:
    root = tree.insert(root=root, key=i)

sol = Solution()
nodes = sol.findTilt(root)
for node in nodes:
    print(node)
