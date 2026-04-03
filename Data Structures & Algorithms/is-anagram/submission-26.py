class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS, lenT= len(s), len(t)
        countS, countT = {}, {}

        if lenS != lenT:
            return False

        for i in range(lenS):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 +  countT.get(t[i], 0)

        return countS == countT


        