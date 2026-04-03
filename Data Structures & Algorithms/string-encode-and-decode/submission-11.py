class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result +=  str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        #first l is to create a while loop
        result = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            result.append(s[l:r])
            l = r
        return result


        # we set other one as r 
        # we will increament until it hits the special char
        # then we get the length by them
        # l = r + 1
        # r = l + length
        #then we will append into the result
        # l = r
        #then result
       
