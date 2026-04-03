class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                currentLength = 0
                while num + currentLength in numsSet:
                    currentLength += 1
                result = max(currentLength, result)
        return result 






        