class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicates = set()

        for num in nums:
            if num in hasDuplicates:
                return True
            hasDuplicates.add(num)
        return False
            
        