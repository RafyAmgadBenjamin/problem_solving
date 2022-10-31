class Solution:
    def missingNumber(self, nums):
        nums.sort()
        if len(nums) == 1 and nums[0] == 0:
            return 1  
        if len(nums) >= 1 and nums[0] == 1:
            return 0 
        if nums[-1] != len(nums):
            return len(nums)

        for i in range(len(nums)-1):
            if nums[i] + 1 != nums[i+1] :
                return nums[i] + 1

        
s = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))