class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #We create a frequency counter where we count number character at each
        #then we retunr counters == to counter t where their boht equal

        #ALso we will return false when the lenght of s and t are not the same

        if len(s) != len(t):
            return False

        
        countT = {}
        countS = {}


        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0 ) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
        