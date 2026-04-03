class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #First is create a frequncy character based alphabet which is from 0 * 26
        #Based on the current counter you will append base on the current string from ord of c - ord "a" and increment by 1
        #Then return a list of of values

        groupingAnagram = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            groupingAnagram[tuple(counter)].append(s)
        
        return list(groupingAnagram.values())

            
        