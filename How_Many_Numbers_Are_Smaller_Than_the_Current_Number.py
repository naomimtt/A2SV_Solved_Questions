class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_array = sorted(nums)
        count = {}
        for i, num in enumerate(new_array):
            if num  in count:
                count[num] = i
        return [count[num] for num in nums]
        

