class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = defaultdict(list)

        for word in strs:
            countCharacter = [0] * 26
            for character in word:
                countCharacter[ord('a') - ord(character)] += 1
            group_anagram[tuple(countCharacter)].append(word) 
        return list(group_anagram.values())