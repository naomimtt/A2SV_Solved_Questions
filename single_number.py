class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            output = output ^ num
        return output 

        # 100 ^ 000 100 4
        # 100 ^ 001 101 1
        #101 ^ 010 111 2
        #111 ^ 001 110 1
        #110 ^ 010 100 2

        #100 ^ 010 110
