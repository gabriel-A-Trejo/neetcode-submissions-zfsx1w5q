class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if s and t are different then return false
        #create a frequency counter s and t using an object
        #check to see if the frequency counter are the same else is return false
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countT == countS
   