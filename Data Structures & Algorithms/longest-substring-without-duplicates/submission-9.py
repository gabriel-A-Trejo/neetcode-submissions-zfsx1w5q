class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        result = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            result = max(result, r - l + 1)
            hashset.add(s[r])
           
        return result
            
            

        