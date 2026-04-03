class Solution:

    def encode(self, strs: List[str]) -> str:
        #we create loop where we get word and use special characters
        #We append as a result
        result = ""

        for s in strs:
            result += str(len(s)) + '#'  + s
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            i = j + 1
            j = i + length
            result.append(s[i : j])
            i = j
        return result


