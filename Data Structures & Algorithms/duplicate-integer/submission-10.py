class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #check to see if the number is not in the set
        #if the intenger is in the set then return false
        #if no number is in the set then return true

        contains = set()

        for num in nums:
            if num in contains:
                return True
            contains.add(num)
        return False

         