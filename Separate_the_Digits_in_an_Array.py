class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new = []
        for num in nums:
            for char in str(num):
                new.append(int(char))
        return new
       
        
        



        
