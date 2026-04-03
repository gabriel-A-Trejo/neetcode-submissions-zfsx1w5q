class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #plan
        #first we need to do a freauency counter but since is lower case leters then we will do 26. hRcters and ghe we can able to count based on it since we can return at any order 
        #Return freuwncy based on it
        Groupgrams = defaultdict(list)

        for s in strs:
            characterCounter = [0] * 26
            for c in s:
                characterCounter[ord("a") - ord(c)] += 1
            Groupgrams[tuple(characterCounter)].append(s)
        return list(Groupgrams.values())



        