class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        hashmap = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s: 
                counter[ord(c) - ord("a")] += 1
            hashmap[tuple(counter)].append(s)
        return list(hashmap.values())
            

        