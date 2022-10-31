class Solution:
    def maxProfit(self, prices):
        accum = 0
        max_profit = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff + accum < 0:
                accum  = 0 
            else: 
                accum += diff

            if accum > max_profit:
                max_profit = accum
        return max_profit

s = Solution()
prices = [7,6,4,3,1]
print(s.maxProfit(prices))