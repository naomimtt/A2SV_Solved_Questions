class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = {}
        sum = 0
        for i in chars:
            count[i] = count.get(i, 0) + 1
        for word in words:
            count2 = {}
            valid = True
            for letter in word:
                count2[letter] = count2.get(letter, 0) + 1
            for letter, value in count2.items():
                if value <= count.get (letter, 0):
                    continue
                else:
                    valid = False
            if valid :
                sum += len(word)
        return sum


                
