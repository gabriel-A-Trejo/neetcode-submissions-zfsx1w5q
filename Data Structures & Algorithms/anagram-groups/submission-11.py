class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_Frequency = defaultdict(list)
        for word in strs:
            countCharacter = [0] * 26
            for character in word:
                countCharacter[ord('a') - ord(character)] += 1
            group_Frequency[tuple(countCharacter)].append(word)
        return list(group_Frequency.values())