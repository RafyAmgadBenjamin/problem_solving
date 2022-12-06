class Solution(object):
    
    # def __init__(self):
    #     # self.nodesCount = 0.0 
    #     # self.total = 0.0
        
    def minDepth(self, root):
            if(root==None):
                return 0
            else:
                lh,rh=self.minDepth(root.left),self.minDepth(root.right)
                if(lh==0 or rh==0):
                    return 1+max(lh,rh)
                else:
                    return 1+min(lh,rh)