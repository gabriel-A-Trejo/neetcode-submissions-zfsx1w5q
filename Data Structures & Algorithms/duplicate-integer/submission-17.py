class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input list of ints

        #Example: nums = [1, 2, 2, 4] will true
        #example 2: nums[] output will be false
        #edge case will be if nums empty return false

        #DSA: set the reason for the set check to see it already containts in the set
        #algorithm
        #first part is to check to see if nums is empty then return false - edge case
        #second part traverse the the list and append to set if only if the current index already has same integer inside the set then return True
        #else return false is there only unique in the set'

        isSet = set()
        if not nums: return False
        for num in nums:
            if num in isSet:
                return True
            isSet.add(num)
        return False
        
                                    
        #output: bool
         