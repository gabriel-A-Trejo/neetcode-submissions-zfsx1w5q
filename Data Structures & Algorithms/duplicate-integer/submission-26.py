class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #First is to create a nums set based around it

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        