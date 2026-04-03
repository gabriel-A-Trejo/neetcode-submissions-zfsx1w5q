class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashNums = set(nums)
        longest = 0

        for num in hashNums:
            if (num - 1) not in hashNums:
                length = 1
                while (num + length) in hashNums:
                    length += 1
                longest = max(length, longest)
        return longest




        