class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        counterT, window = {}, {}

        for c in t:
            counterT[c] = 1 + counterT.get(c, 0)

        result, resultLen = [-1, -1], float("inf")
        have, need = 0, len(counterT)

        l = 0
        for r in range(len(s)):
            currentR = s[r]
            window[currentR] = 1 + window.get(currentR, 0)

            # FIX 1
            if currentR in counterT and window[currentR] == counterT[currentR]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < resultLen:
                    result = [l, r]
                    resultLen = r - l + 1

                # remove left character
                currentL = s[l]
                window[currentL] -= 1

                if currentL in counterT and window[currentL] < counterT[currentL]:
                    have -= 1

                l += 1

        l, r = result
        return s[l:r+1] if resultLen != float("inf") else ""

        