class Solution:
    def singleNumber(self, nums):
        counters = {}
        for num in nums: 
            if num not in counters:
                counters[num] = 1
            else:
                counters[num] += 1 

        results = []
        for k,v in counters.items():
            if v < 2:   
                results.append(k)
        return results[0]
        
s = Solution()
nums = [4,1,2,1,2]
print(s.singleNumber(nums))