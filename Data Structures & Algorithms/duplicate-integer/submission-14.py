class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Example 1: nums = [1, 2, 3, 3] : true
        #Example 2: nums = [1, 2, 3, 4] : false

        numSet = set()

        for num in nums:
            if num in numSet: return True
            numSet.add(num)
        return False
         