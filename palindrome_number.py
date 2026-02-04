class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal=str(x)
        pal2= pal[::-1]
        if pal==pal2:
            return True
        else:
            return False 
