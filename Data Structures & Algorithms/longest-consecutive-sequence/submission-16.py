class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        setNums = set(nums)
        result = 0
        for num in setNums:
            if num - 1 not in setNums:
                longest = 0
                while num + longest in setNums:
                    longest += 1
                    result = max(result, longest)
        return result