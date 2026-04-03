class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Data structure is set
        contains = set()
        #First step is traverse the list
        for n in nums:
            #check to see if the current is in the set then return else we add it in the set if not in the set
            if n in contains:
                return True
            contains.add(n)
        #when the loops ends return fasle
        return False
            

         