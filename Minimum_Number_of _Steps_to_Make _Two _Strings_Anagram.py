class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        count2 = Counter(t)
        if count == count2:
            return 0
        counter = 0
        for char in count2:
            if count2[char] > count.get(char, 0):
                counter += count2[char] - count.get(char, 0)
        return counter
        

        
