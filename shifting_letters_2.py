class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        new = list(s)
        prefix = [0 for _ in range(len(new))]
        for l, r, d in shifts:
            if d == 0:
                prefix[l] -= 1
                if r+1 < len(new):
                    prefix[r+1] += 1
            else:
                prefix[l] += 1
                if r+1 < len(new):
                    prefix[r+1] -= 1

        prefix_sum = []
        prefix_sum.append(prefix[0])
        for i in range(1, len(prefix)):
            prefix_sum.append(prefix[i]+prefix_sum[-1])

        for i in range(len(prefix_sum)):
            new[i] = chr(((ord(new[i]) - ord('a') + prefix_sum[i]) % 26 )+ 97)

        return ''.join(new)




       

        
