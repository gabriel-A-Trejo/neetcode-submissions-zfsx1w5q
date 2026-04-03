class Solution:

    def encode(self, strs: List[str]) -> str:
        #List -> str

        #Plan

        #create a for loop and we can able to get length of string with key length + something + string and we will concatinate
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result


    def decode(self, s: str) -> List[str]:
        #if no s return empty list 
        result = []
        if not s:
            return []

        #We will use left to start at 0 when in that 0 we will able to get which we will use while < len(s)
        #After that we will use  called right when and we can move right to right when it has a speical character
        #We will calculate the length then we increment left to right + 1 then we will add  then right = left + lenghth
        #we will used that as result in the list

        left = 0
        while left < len(s):
            right = left 
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = length + left
            result.append(s[left:right])
            left = right
        return result


