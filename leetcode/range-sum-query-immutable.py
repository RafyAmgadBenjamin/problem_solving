class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])


        # Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.nums)
print(obj.sumRange(2, 5))

# param_1 = obj.sumRange(left,right)
