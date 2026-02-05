class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums = set(nums)
        for i in range(0, n + 1):
            if i in nums:
                continue
            return i
        
