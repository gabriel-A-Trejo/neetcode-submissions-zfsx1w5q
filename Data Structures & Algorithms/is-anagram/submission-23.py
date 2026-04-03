class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        lengthT = len(t)
        countS = {}
        countT = {}

        if lengthS != lengthT:
            return False

        for i in range(lengthS):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    
        