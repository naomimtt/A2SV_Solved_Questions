class Solution:
    def findValidPair(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1
        for i in range(len(s) - 1):
            if s[i] != s[i+1] and int(s[i]) == count[s[i]] and int(s[i + 1]) == count[s[i + 1]]:
                return s[i] + s[i+1]
        return ""
         

        
