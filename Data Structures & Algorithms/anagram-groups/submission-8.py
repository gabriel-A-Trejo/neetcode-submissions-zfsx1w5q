class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #list of strings

        #Example : act, pots, tops ->  We can able to use a frequency counter to count number of strings that will are equal between the number counts
        #For counter we can able to use 0 * 26 based on the order of current c if it is lower case
        #append the current counter
        
        hashmap = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            hashmap[tuple(counter)].append(s)
        return list(hashmap.values())

        #output is list of list
        