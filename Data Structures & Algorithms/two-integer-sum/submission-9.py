class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        complement = 0
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in hashmap:
                return [hashmap[complement], index]
            hashmap[nums[index]] = index

