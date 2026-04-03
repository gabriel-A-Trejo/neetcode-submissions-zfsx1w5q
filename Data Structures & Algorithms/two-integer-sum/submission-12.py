class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        getIndexes = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in getIndexes: return [getIndexes[complement], i]
            getIndexes[nums[i]] = i
        return [-1]
        

        