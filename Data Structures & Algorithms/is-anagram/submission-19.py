class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Data structure will be a dictionary since is anagram we need to check if the lenght of both are the same
        #if is the same then we will contiune else we automaticly return false after that we will create a range based length of the string
        #we will count number of characters based on the dictirionary after we will check to see if both are the same else return false

        countT, countS = {}, {}
        lengthS = len(s)
        lenghtT = len(t)

        if lengthS != lenghtT:
            return False

        for i in range(lengthS):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countT == countS