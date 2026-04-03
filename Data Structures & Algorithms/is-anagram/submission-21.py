class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_of_s = len(s)
        length_of_t = len(t)
        countT = {}
        countS = {}

        if length_of_s != length_of_t:
            return False

        for i in range(length_of_s):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countT == countS