class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input is list of string
        #output a list of list of strings

        #edge case if the stirng is empty
        if not strs:
            return [[]]

        #inteview question:
        #if all lower case and now special charaacters?

        #DSA: dictioary | counter:list of strings
        res = defaultdict(list)
        #counter will be a list of ints 



        #Steps 
        #two for loops one for string and another for counter frequency
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            res[tuple(counter)].append(s)
        return list(res.values())



