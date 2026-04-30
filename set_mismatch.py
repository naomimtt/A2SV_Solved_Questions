class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        uni = set()
        duplicate = -1
        for num in nums:
            if num in uni:
                duplicate = num
            uni.add(num)
         
        for i in range(1, len(nums) + 1):
            if i not in uni:
                missing = i
                break
        
        return [duplicate, missing]
