class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        #input of list of int
        #output is bool:
        
        #edge case is empty return false
        if not nums: return False


        #create a for loop
        #DSA is set and we will check if the set is already contains it
        isDuplicate = set()
        #if already contains it return true and return false when there is no duplicate
        for num in nums:
            if num in isDuplicate:
                return True
            isDuplicate.add(num)
        return False
        
        

         