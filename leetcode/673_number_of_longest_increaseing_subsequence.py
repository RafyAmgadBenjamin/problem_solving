class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        lengths = [1] * n  # lengths[i]: length of LIS ending at index i
        counts = [1] * n   # counts[i]: number of LIS ending at index i

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)  # Length of the longest increasing subsequence
        result = 0

        # Count the number of LIS with the maximum length
        for i in range(n):
            if lengths[i] == max_length:
                result += counts[i]

        return result
        