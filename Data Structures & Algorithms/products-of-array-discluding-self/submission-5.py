class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        previous = 1
        for i in range(len(nums)):
            result[i] = previous
            previous *= nums[i]

        Future = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= Future
            Future *= nums[i]

        return result

        