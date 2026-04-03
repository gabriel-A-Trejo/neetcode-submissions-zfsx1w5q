class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexByValue = {}
        for i in range(len(nums)):
            current = nums[i]
            needed = target - current
            if needed in indexByValue:
                return [indexByValue[needed], i]
            indexByValue[nums[i]] = i
        return [-1, -1]
        