class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counterFrequency = {}
        l = 0

        maxFrequency = 0

        result = 0

        for r in range(len(s)):
            counterFrequency[s[r]] = 1 + counterFrequency.get(s[r], 0)
            maxFrequency = max(maxFrequency, counterFrequency[s[r]])
            
            while (r - l + 1) - maxFrequency > k:
                counterFrequency[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
            

            

