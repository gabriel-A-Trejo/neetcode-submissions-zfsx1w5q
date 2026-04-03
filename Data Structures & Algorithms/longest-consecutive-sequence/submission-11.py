class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = set(nums)
        result = 0

    
        for num in longest:
            streak, current = 0, num
            while current in longest:
                current += 1
                streak += 1
            result = max(result, streak)

        return result