class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = []
        prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        mini = min(prefix_sum)
        if mini > 0:
            return 1
        else:
            return abs(mini) + 1
            

        
