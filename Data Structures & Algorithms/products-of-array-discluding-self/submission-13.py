class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lengthNums = len(nums)
        result = [1] * lengthNums
        
        prefix = 1
        for i in range(lengthNums):
            result[i] = prefix
            prefix *= nums[i]
        
        posfix = 1
        for i in range(lengthNums - 1, -1, -1):
            result[i] *= posfix
            posfix *= nums[i]
        return result