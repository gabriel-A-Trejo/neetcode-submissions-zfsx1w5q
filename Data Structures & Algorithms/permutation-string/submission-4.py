class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Length = len(s1)
        s2Length = len(s2)

        counterS1 = [0] * 26
        counterS2 = [0] * 26

        if s1Length > s2Length:
            return False

        for i in range(len(s1)):
            counterS1[ord(s1[i]) - ord('a')] += 1
            counterS2[ord(s2[i]) - ord('a')] += 1

        if counterS1 == counterS2:
            return True

        for r in range(s1Length, s2Length):
            counterS2[ord(s2[r]) - ord('a')] += 1
            counterS2[ord(s2[r - s1Length]) - ord('a')] -= 1

            if counterS1 == counterS2:
                return True

        return False

