class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #First thing is to have hashmap = defaultDict by list
        hashmap = defaultdict(list)

        #the key will be the frequency counter where  there will have 26 lower case letters
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            hashmap[tuple(counter)].append(s)
        return list(hashmap.values())

        #since keys are inmutable we can able to added in as a tuple 

        #first step is create hashmap

        #create loop for the strings
        #Create a counter where [0] * 26
        #create loop by characters where we can have ord 97 - 122 = + 1

        #then after the loop append the hashmap as a key then current word

        #then return a listbased on the values



        