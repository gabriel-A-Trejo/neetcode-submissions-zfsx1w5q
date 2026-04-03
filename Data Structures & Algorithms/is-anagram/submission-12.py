class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input s: string 
        #input t: string 
        #output is bool

        #Edge cases: 
            #if there not the the same size then return false
            if len(s) != len(t): return False

            #DSA: dictionary: char: int
            sCounter = {}
            tCounter = {}
            
            #Create a counter frequency for both and return if all counter frequency are equal to each other then return True and false
            for i in range(len(s)):
                sCounter[s[i]] = 1 + sCounter.get(s[i], 0)
                tCounter[t[i]] = 1 + tCounter.get(t[i], 0)
            return sCounter == tCounter





        