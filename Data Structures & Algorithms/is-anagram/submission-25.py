class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengnthS, lengthT, = len(s), len(t)

        if lengnthS != lengthT:
            return False

        countS, countT = {}, {}

        for i in range(lengnthS):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT


