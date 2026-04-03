class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Understanding we need calculate only when nums[i]

        #we can intialize result to all 1 then we times it based on the prefix
        result = [1] * len(nums)
        
        prefix = 1
        #Create for loop that we multiple prefix based on current value in that list
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        #next thing we can able to reverse which we can able to do based on it
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
