class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros = 0, 0
        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1
            if zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
        return len(nums) - left - 1
