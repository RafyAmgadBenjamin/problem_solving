class Solution(object):
    
    def __init__(self):
        self.nodesCount = 0.0 
        self.total = 0.0
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = self.height(root)
        averages = []
        for level in range(levels+1):
            self.total = 0.0
            self.nodesCount = 0.0
            self.BFS(root, level)
            if self.nodesCount > 0:
                averages.append(self.total/self.nodesCount)
        
        return averages

    def BFS(self, root, level):
        if not root:
            return
        elif (level == 1):
            self.total += root.val
            self.nodesCount += 1
        elif (level > 1):
            self.BFS(root.left, level-1)
            self.BFS(root.right, level-1)


    def height(self, root):
        if not root:
            return 0
        else:
            l = self.height(root.left)
            r = self.height(root.right)
            if l > r :
                return (l + 1)
            else:
                return(r + 1)
