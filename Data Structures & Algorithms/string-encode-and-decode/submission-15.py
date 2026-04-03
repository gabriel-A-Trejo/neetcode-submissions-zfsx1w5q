class Solution:

    def encode(self, strs: List[str]) -> str:
        array_to_string = ""
        for word in strs:
            array_to_string += str(len(word)) + "#" + word 
        return array_to_string

    def decode(self, s: str) -> List[str]:
        string_to_array = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            getLength = int(s[i:j])
            i = j + 1
            j = i + getLength
            string_to_array.append(s[i:j])
            i = j
        return string_to_array

           
            