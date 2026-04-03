class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for char in t:
            d[char] += 1
        l = r = 0
        formed, total = 0, len(d)
        result = float('inf')
        subL, subR = 0, 0
        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    formed += 1
            while l <= r and formed == total:
                currentLength = r - l + 1
                if currentLength < result:
                    result = currentLength
                    subL, subR = l, r + 1
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1
                l += 1
            r += 1
        return "" if result == float('inf') else s[subL: subR]
        