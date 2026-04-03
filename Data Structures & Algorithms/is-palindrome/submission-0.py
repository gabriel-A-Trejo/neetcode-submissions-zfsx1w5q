class Solution:
    def isPalindrome(self, s: str) -> bool:

        #We will create two pointer as r is to the right and l is at the beginning
        l = 0
        r = len(s) - 1

        #We will traverse when  r > l or l < r and when to  break the loop:
        while l < r:
            #This is to skip white spaces or !, ..., ?, etc
            #incrementations l += 1 | so when l < r then we check in isLetterOrNumber
            while l < r and not self.isLetterOrNumber(s[l]):
                l += 1
            #decrement r when r > l
            while r > l and not self.isLetterOrNumber(s[r]):
                r -= 1
            #check to see if current position of L and R does not have the same character to return false and put in lowercase if the character is are captilizae or one of them is
            if s[l].lower() != s[r].lower():
                return False
            #We increment L and decrement R for the loop to repeat
            l += 1
            r -= 1
        return True


        

    #first thing how can we able to break the character down and check to see is there any space and question marks
    def isLetterOrNumber(self, char):
        return (ord("A") <= ord(char) <= ord("Z") or
                ord("a") <= ord(char) <= ord("z") or 
                ord("0") <= ord(char) <= ord("9"))