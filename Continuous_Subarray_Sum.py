class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = []
        prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        remainder = {0: -1}

        for i in range(len(nums)):
            if prefix_sum[i] % k in remainder:
                if abs(remainder[prefix_sum[i] % k]  - i) >= 2:
                    return True
            else:
                remainder[prefix_sum[i] % k] = i
        return False



        
