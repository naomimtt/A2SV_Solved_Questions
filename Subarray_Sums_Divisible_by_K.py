class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        mapp = {0:1}
        for num in nums:
            prefix += num
            mod = prefix % k
            if mod < 0:
                mod += k
            if mod in mapp:
                count += mapp[mod]
                mapp[mod] += 1
            else:
                mapp[mod] = 1
        return count
        

        
