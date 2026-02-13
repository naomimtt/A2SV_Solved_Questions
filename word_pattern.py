class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        letter_to_word = {}
        word_to_letter = {}
        for p, w in zip(pattern, words):
            if p in letter_to_word:
                if letter_to_word[p] != w:
                    return False
            else:
                letter_to_word[p] = w
            if w in word_to_letter:
                if word_to_letter[w] != p:
                    return False
            else:
                word_to_letter[w] = p
        return True
        

        
