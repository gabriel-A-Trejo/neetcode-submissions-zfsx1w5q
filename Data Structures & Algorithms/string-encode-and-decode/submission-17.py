class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        l, r = 0, 0
        while l < len(s):
            l = r
            while s[r] != "#":
                r += 1
            getLength = int(s[l:r])
            l = r + 1
            r = l + getLength
            getWord = s[l:r]
            result.append(getWord)
            l = r
        return result

