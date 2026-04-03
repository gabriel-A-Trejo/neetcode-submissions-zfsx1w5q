class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Length = len(s1)
        s2Length = len(s2)

        if s1Length > s2Length:
            return False

        counters1 = [0] * 26
        counters2 = [0] * 26

        # Build frequency for s1 and first window of s2
        for i in range(s1Length):
            counters1[ord(s1[i]) - ord('a')] += 1
            counters2[ord(s2[i]) - ord('a')] += 1

        if counters1 == counters2:
            return True

        # Sliding window
        for r in range(s1Length, s2Length):
            counters2[ord(s2[r]) - ord('a')] += 1
            counters2[ord(s2[r - s1Length]) - ord('a')] -= 1

            if counters1 == counters2:
                return True

        return False

        