class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        freq = [0] * (n + 1)

        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1

        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq = freq[:n]

        nums.sort()
        freq.sort()

        result = 0
        for i in range(n):
            result = (result + nums[i] * freq[i]) % MOD

        return result
