class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #First we check the s and t are in the same lenght
        if len(s) != len(t):
            return False
        
        #Next step is to create a frequency counter and return if the counter map has the same value based on the key.
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT