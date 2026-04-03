class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #We will create an hashset
        hashset = set()

        #Create a for loop 
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

        #if the curr is hash set then return true

        #added in the hasSet

        #when is completed return false
        