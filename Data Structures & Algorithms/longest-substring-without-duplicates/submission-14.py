class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hasSeen = set()
        result = 0

        for r in range(len(s)):
            while s[r] in hasSeen:
                hasSeen.remove(s[l])
                l += 1
            
            result = max(result, r - l + 1)
            hasSeen.add(s[r])
        return result

            

        