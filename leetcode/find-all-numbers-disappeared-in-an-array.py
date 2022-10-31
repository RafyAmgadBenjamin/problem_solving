class Solution:
    def findDisappearedNumbers(self, nums):
        max_no = len(nums)
        numbers = {}
        results = []
        for num in nums:
            numbers[num]= True
        
        for i in range(1,max_no+1):
            if i not in numbers:
                results.append(i)
        return results

s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))