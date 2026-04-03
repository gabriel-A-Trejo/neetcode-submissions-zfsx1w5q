class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        isInNums = set(nums)
        result = 0
        

        for num in nums:
            longest = 0
            while num + longest in isInNums:
                longest += 1
            result = max(result, longest)
        return result
                  