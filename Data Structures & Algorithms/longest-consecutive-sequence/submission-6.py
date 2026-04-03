class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        for num in nums:
            current_length = 1
            if num - 1 in nums:
                while num - current_length in nums:
                    current_length += 1
            max_length = max(max_length, current_length)
            
        return max_length


