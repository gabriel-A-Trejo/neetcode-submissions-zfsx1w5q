class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #let check to see if they are in the same length
        if len(s) != len(t):
            return False
        #if not then return false

        countS = {}
        countT = {}

        #create for loop
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        #we use a count frequency

        return countS == countT 


        #then we will return when s == j based on the counter Frequency
        