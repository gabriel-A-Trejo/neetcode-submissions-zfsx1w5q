class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in numSet:
            if num - 1 not in numSet:
                longest = 1
                while num + longest in numSet:
                    longest += 1
                result = max(result, longest)
        return result

