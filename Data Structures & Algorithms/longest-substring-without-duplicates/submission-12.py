class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        hashSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            result = max(result, (r - l) + 1)
            hashSet.add(s[r])
           
        return result
        
            
        


        