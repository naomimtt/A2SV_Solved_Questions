class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                out.append(nums[i])
        return out
