class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index_by_list_of_frequency = defaultdict(list)

        for word in strs:
            counter = [0] * 26
            for character in word:
                counter[ord(character) - ord("a")] += 1
            index_by_list_of_frequency[tuple(counter)].append(word)
        return list(index_by_list_of_frequency.values())