class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter()
        for day in responses:
            count.update(set(day))  
        max_count = max(count.values())
        return min(resp for resp, c in count.items() if c == max_count)
