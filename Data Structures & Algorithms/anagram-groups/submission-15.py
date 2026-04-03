class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            hashmap[tuple(counter)].append(s)
        return list(hashmap.values())
               


        #Create a for loop so we will create a frequency counter based since
        #We a all lower case we can able to count based on it and get all lower case letters based on it
        #We will count based on the number of character then result to the append on the value adn have a dict return based on it


        #return a list of values based on it
        