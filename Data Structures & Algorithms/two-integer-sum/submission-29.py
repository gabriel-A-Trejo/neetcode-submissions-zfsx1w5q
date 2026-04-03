class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasSeen = {}
        
        for index, value in enumerate(nums):
            complement = target - value

            if complement in hasSeen:
                return [hasSeen[complement], index]
            hasSeen[value] = index
        return [-1, -1]
        