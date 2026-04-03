class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Exact same CHAR, order can be different based on a object
        #Let see if s and t are in the same length
        if(len(s) != len(t)): return False
        counterS = {}
        counterT = {}
        #Since we have two inputes of different strings what we can since it will O(a + N)
        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)

        return counterS == counterT
        