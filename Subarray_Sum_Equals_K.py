class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k
            if needed in count:
                result += count[needed]

            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        return result
