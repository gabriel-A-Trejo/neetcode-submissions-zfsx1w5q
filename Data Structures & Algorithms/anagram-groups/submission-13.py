class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Createn a hashmap called anagrams with a default key of list
        hashmap = defaultdict(list)

        #Create a loop by strings
        for s in strs:
           #since is all lowercase letters we can put upto 26 characters
           countChar = [0] * 26
           for c in s:
               countChar[ord(c) - ord('a')] += 1
           hashmap[tuple(countChar)].append(s)
        return list(hashmap.values())
    
        

        #Create a loop by characters
             #create a counter frequency
        
        #Append based counter as keys [] then we will append the s

        #then return a list based on the values

    
        