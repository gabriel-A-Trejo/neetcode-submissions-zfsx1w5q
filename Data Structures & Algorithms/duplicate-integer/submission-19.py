class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        doesItContainDuplicates = set()
        for num in nums:
            if num in doesItContainDuplicates:
                return True
            doesItContainDuplicates.add(num)
        return False
        