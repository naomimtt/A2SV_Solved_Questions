class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        window = set()
        left, right = 0, 0
        longest = 0

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
            else:
                window.remove(s[left])
                left += 1

        return longest
