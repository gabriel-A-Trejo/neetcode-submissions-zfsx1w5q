class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        LOWER_CASE_COUNT = 26
        INTILIZE = 0
        result = defaultdict(list)

        for word in strs:
            character_counter = [INTILIZE] * LOWER_CASE_COUNT
            for character in word:
                character_counter[ord(character) - ord('a')] += 1
            key = tuple(character_counter)
            result[key].append(word)
        return list(result.values())


        