class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #We need to check to see if the lenght of s and lenght of are not the same then retutnr False
        #We we create frequency counter for both when they both are in equal lenght

        if len(s) != len(t):
            return False

        #Counter freq
        counterS = {}
        counterT = {}

        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1

        #we added until the end loop
        return counterT == counterS

        #then we end return when coutnerT == CounterS
        