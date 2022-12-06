# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from __future__ import annotations


class Solution:
    def __init__(self):
        self.accum = 0 
        self.targetSum = 0
    def hasPathSum(self, root, targetSum):
        self.targetSum = targetSum
        def DFS(root):
            if root:
                self.accum += root.val
                if not root.left and not root.right: # no children (end of path)
                    if self.accum == self.targetSum:
                        return True
                    else:
                        self.accum -= root.val
                        return False
                l = DFS(root.left)
                r = DFS(root.right)
                self.accum -= root.val
                return l or r
        return DFS(root)

s = Solution()
s.hasPathSum(None, 13)
