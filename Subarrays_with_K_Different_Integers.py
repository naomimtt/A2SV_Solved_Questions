class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        left1 = left2 = 0

        for right in range(n):

            freq1[nums[right]] += 1

            freq2[nums[right]] += 1

            while len(freq1) > k:
                freq1[nums[left1]] -= 1
                if freq1[nums[left1]] == 0:
                    del freq1[nums[left1]]
                left1 += 1

            while len(freq2) > k - 1:
                freq2[nums[left2]] -= 1
                if freq2[nums[left2]] == 0:
                    del freq2[nums[left2]]
                left2 += 1

            count += left2 - left1

        return count
