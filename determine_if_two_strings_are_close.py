class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count = Counter(word1)
        count2 = Counter(word2)
        if set(count.keys()) != set(count2.keys()):
            return False
        if sorted(count.values()) != sorted(count2.values()):
            return False
        return True
        



        
