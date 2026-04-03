class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_frequency_list = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for character in word:
                count[ord('a') - ord(character)] += 1
            count_frequency_list[tuple(count)].append(word)
        
        return list(count_frequency_list.values())