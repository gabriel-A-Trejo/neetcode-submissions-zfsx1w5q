class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input: s: string t: string

        #example: car and rac  since it car and rac contains one c, and one a, and on c from both then return true
        #example: cat and Dog since c contain one but D does nto contain in s then return False
        #Asking the interviewer: is only lower case and does it containing white spaces
        #example 3: what if s and t has different length then will be false given the definition anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        #then return false


        #edge case: when s and t are different length or one of them are empty
        #DS: dictionary since wee need to keep count number character are in that particaly s or t
        #algorithm: 
        #step 1 check to see if s and t have the same length and are they are not empty
        #since if they alredy same length then we can use one for loop to traverse and count the number of characters
        #last step: when counter of s and counter t == then return true else false


        if len(s) != len(t) or not s or not t: return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT





        #output: bool
        