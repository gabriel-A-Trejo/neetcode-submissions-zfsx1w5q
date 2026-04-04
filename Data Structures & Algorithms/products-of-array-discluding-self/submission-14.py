class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        result = [1] * lenNums

        prefix = 1
        for i in range(lenNums):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(lenNums - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
        
        