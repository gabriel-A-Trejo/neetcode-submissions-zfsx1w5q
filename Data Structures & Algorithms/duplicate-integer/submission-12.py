class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #First we create a set
        #WE will traverse if the nums contains the set then return true 
        #else return false if nums list has been traverse completly

        contain = set()

        for num in nums:
            if num in contain:
                return True
            contain.add(num)
        return False
         