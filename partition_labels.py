class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = []
        last_occurence = {char: index for index, char in enumerate(s)}
        start, end = 0, 0
        for index, char in enumerate(s):
            end = max(end, last_occurence[char])
            if index == end:
                size.append(end - start + 1)
                start = index + 1
        return size 



        
