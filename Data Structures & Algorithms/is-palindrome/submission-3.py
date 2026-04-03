class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        #Set left right to 0 and by the lgnth

        #Whule l < r:

        #quicj return false when they are not equal

        #when lop finish return true

        l, r = 0, len(s) - 1

        while l < r:
            if (s[l] != s[r]):
                return False
            l+= 1
            r -= 1
        return True
        