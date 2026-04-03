class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isSeen = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in isSeen:
                return [isSeen[complement], index]
            isSeen[value] = index
        
        