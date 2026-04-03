class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            currentSum = target - nums[i]

            if currentSum in seen:
                return [seen[currentSum], i]
            seen[nums[i]] = i
        return [-1, -1]