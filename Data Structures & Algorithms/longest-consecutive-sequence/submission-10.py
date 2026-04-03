class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        hashNums = set(nums)

        for num in hashNums:
            if num - 1 not in hashNums:
                length = 1
                while num + length in hashNums:
                    length += 1
                result = max(result, length)
        return result



        