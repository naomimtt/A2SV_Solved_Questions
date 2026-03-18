class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ppl = [i+1 for i in range(n)]
        current = 0
        while len(ppl) > 1:
            current = (current+k-1) % len(ppl)
            ppl.pop(current)
        return ppl[0]
        





        
