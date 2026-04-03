class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        contain = defaultdict(list)

        #First we will traverse and use another counter to traverse 
        for string in strs:
            #lets create counter variable
            counter = [0] * 26
            #A frequency counter
            for char in string:
                counter[ord(char) - ord('a')] += 1
            contain[tuple(counter)].append(string)
        
        return list(contain.values())


        