class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxFreq = 0
        l = 0
        result = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
        