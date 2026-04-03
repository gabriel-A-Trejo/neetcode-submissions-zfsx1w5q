class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listdict = defaultdict(list)
        

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            listdict[tuple(counter)].append(s)
        return list(listdict.values())

        