class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in index:
                return [index[complement], i]
            index[n] = i
        