class Solution:
    def countBits(self, n):
        values = []
        for i in range(n+1):
            values.append(bin(i)[2:].count('1'))
        return values

s = Solution()
print(s.countBits(5))        