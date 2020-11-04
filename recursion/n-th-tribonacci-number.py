class Solution:
    memo = {}

    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        elif n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            res = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            self.memo[n] = res
            return res


s = Solution()
print(s.tribonacci(25))
