class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            countWord = [0] * 26
            for char in word:
                countWord[ord(char) - ord('a')] += 1
            result[tuple(countWord)].append(word)
        return list(result.values())
        