class Solution:
    def containsDuplicate(self, nums):
        sums = {}
        for val in nums:
            if val not in sums:
                sums[val] = 0 
            else:
                return True
        return False
            

s = Solution()
nums = [1,2,3,1]
print(s.containsDuplicate(nums))