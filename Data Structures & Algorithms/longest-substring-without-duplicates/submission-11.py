class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueString = set()
        result = 0
        l = 0
        for r in range(len(s)):
            while s[r] in uniqueString:
                uniqueString.remove(s[l])
                l += 1
            result = max((r - l) + 1, result)
            uniqueString.add(s[r])
        return result
        

        