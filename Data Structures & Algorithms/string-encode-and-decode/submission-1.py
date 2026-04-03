class Solution:

    def encode(self, strs: List[str]) -> str:
        #first we will traverse the strings
        #We will have a count with the hashmap
        #Next thing is to concate

        concatedString = ""

        for string in strs:
            concatedString += f"{len(string)}#{string}"
        return concatedString


    def decode(self, s: str) -> List[str]:
        #Traverse the stirng 
        container = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i: j])
            i = j + 1
            j = i + length
            container.append(s[i:j])
            i = j
        return container
            
           


