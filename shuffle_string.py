class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res =[''] * len(s)
        for char, idx in zip(s, indices):
            res[idx] = char
        return ''.join(res)
        
