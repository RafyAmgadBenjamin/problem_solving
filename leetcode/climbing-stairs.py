class Solution:
    def climbStairs(self, n):
        mem = {}
        def countStairs(n):
            if n < 0:
                return 0
            if n == 0:
                return 1 

            if n in mem:
                return mem[n]
            else:
                mem[n] = countStairs(n-1) + countStairs(n-2) 
            return  mem[n] 
        return countStairs(n)
        
s = Solution()
print(s.climbStairs(4))