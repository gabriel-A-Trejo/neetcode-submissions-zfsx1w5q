class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isSeen = {}
        lengthNums = len(nums)

        if lengthNums == 0:
            return [-1, -1]
        
        for i in range(lengthNums):
            currentValue = nums[i]
            complement = target - currentValue

            if complement in isSeen:
                return [isSeen[complement], i]
            isSeen[currentValue] = i
        return [-1, -1]